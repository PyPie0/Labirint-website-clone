const sliders2 = {};
document.querySelectorAll('.book-slider2').forEach((slider) => {
	sliders2[slider.className] = new ChiefSlider(slider, {
		loop: true,
		autoplay: true,
		interval: 4000,
		swipe: true,
		refresh: true,
	})
});