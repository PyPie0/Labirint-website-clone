const sliders = {};
document.querySelectorAll('.book-slider2').forEach((slider) => {
	sliders[slider.className] = new ChiefSlider(slider, {
		loop: true,
		autoplay: true,
		interval: 4000,
		swipe: true,
		refresh: true,
	})
});