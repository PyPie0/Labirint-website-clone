const sliders = {};
document.querySelectorAll('.book-slider').forEach((slider) => {
	sliders[slider.className] = new ChiefSlider(slider, {
		loop: true,
		autoplay: true,
		interval: 4000,
		swipe: true,
		refresh: true,
	})
});