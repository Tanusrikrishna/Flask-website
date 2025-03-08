let currentIndex = 0;
const slides = document.querySelector(".slides");
const dots = document.querySelectorAll(".dot");
const totalSlides = dots.length; // Total number of slides

function showSlide(index) {
    if (index >= totalSlides) index = 0; // Loop back to first slide
    if (index < 0) index = totalSlides - 1; // Loop back to last slide

    slides.style.transform = `translateX(-${index * 100}%)`;

    dots.forEach(dot => dot.classList.remove("active"));
    dots[index].classList.add("active");

    currentIndex = index;
}

function nextSlide() {
    showSlide(currentIndex + 1);
}

function prevSlide() {
    showSlide(currentIndex - 1);
}

function goToSlide(index) {
    showSlide(index);
}

// Add event listeners for navigation
document.querySelector(".prev").addEventListener("click", prevSlide);
document.querySelector(".next").addEventListener("click", nextSlide);

// Auto-slide every 3 seconds
setInterval(nextSlide, 3000);
