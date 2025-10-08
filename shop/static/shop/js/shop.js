console.log("shop.js loaded");

document.addEventListener("DOMContentLoaded", () => {
  document.body.style.opacity = 0;
  setTimeout(() => {
    document.body.style.transition = "opacity 0.6s ease";
    document.body.style.opacity = 1;
  }, 50);
});

document.querySelectorAll(".btn-dark").forEach(button => {
  button.addEventListener("click", () => {
    button.classList.add("added");
    button.innerHTML = '<i class="bi bi-check-circle"></i> Added!';
    setTimeout(() => {
      button.classList.remove("added");
      button.innerHTML = '<i class="bi bi-cart-plus"></i> Add to Cart';
    }, 1500);
  });
});

document.querySelectorAll(".btn-outline-danger").forEach(heartBtn => {
  heartBtn.addEventListener("click", (e) => {
    e.currentTarget.classList.toggle("active");
  });
});

const searchBox = document.querySelector('input[name="q"]');
if (searchBox) {
  searchBox.addEventListener("input", function() {
    const query = this.value.toLowerCase();
    document.querySelectorAll(".product-card").forEach(card => {
      const title = card.querySelector(".card-title").textContent.toLowerCase();
      card.parentElement.style.display = title.includes(query) ? "" : "none";
    });
  });
}

const toggle = document.createElement("button");
toggle.className = "btn btn-outline-secondary ms-3";
toggle.innerHTML = '<i class="bi bi-moon"></i>';
document.querySelector(".navbar-nav").appendChild(toggle);

toggle.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  toggle.innerHTML = document.body.classList.contains("dark-mode")
    ? '<i class="bi bi-sun"></i>'
    : '<i class="bi bi-moon"></i>';
  localStorage.setItem("theme", document.body.classList.contains("dark-mode") ? "dark" : "light");
});

window.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
    toggle.innerHTML = '<i class="bi bi-sun"></i>';
  }
});

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".favourite-btn").forEach(btn => {
    btn.addEventListener("click", e => {
      e.preventDefault();

      const heartIcon = btn.querySelector("i");
      btn.classList.toggle("active");

      // Toggle icon style
      if (btn.classList.contains("active")) {
        heartIcon.classList.remove("bi-heart");
        heartIcon.classList.add("bi-heart-fill");
      } else {
        heartIcon.classList.remove("bi-heart-fill");
        heartIcon.classList.add("bi-heart");
      }

      // Optional: send AJAX request to backend to update favourite status
      fetch(btn.getAttribute("href"), { method: "GET" })
        .catch(err => console.error("Favourite toggle failed:", err));
    });
  });
});

document.querySelectorAll(".favourite-btn").forEach(btn => {
    btn.addEventListener("click", e => {
        e.preventDefault();
        const productId = btn.dataset.productId;
        fetch(`/favourites/toggle/${productId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(res => res.json())
        .then(data => {
            const icon = btn.querySelector('i');
            if(data.status === 'added'){
                btn.classList.add('active');
                icon.classList.remove('bi-heart');
                icon.classList.add('bi-heart-fill');
            } else {
                btn.classList.remove('active');
                icon.classList.remove('bi-heart-fill');
                icon.classList.add('bi-heart');
            }
        })
        .catch(err => console.error(err));
    });
});


// CSRF helper for Django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.add-to-cart-btn');

    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.dataset.productId;

            fetch(`/add-to-cart/${productId}/`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Optional: update cart counter in navbar
                    const cartCounter = document.querySelector('#cart-counter');
                    if (cartCounter) cartCounter.textContent = data.total_items;
                } else {
                    alert(data.message);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});