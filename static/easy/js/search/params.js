function change_price(){
	}

$(document).ready(function(){
	$("#params").append('<div style="margin:40px;width:100%;height:3%">\
		<div id="slider" style="width:50%;"></div>\
		<div id="Navigation" style="left:10%;">\
			<ul class="Navigation" >\
            	<li><a href="#">My Portfolio</a>\
					<ul>\
				   		<li><a href="#">Web Development</a></li>\
				   		<li><a href="#">Motion Graphics</a></li>\
				   		<li><a href="#">Flash Animation</a></li>\
                   		<li><a href="#">Logo Design</a></li>\
                   		<li><a href="#">Photography</a></li>\
					</ul>\
			 	</li>\
			 </ul>\
        </div>\
        <<div id="Navigation" style="left:10%;width:10%">\
			<ul class="Navigation" >\
            	<li><a href="#">My Portfolio</a>\
					<ul>\
				   		<li><a href="#">Web Development</a></li>\
				   		<li><a href="#">Motion Graphics</a></li>\
				   		<li><a href="#">Flash Animation</a></li>\
                   		<li><a href="#">Logo Design</a></li>\
                   		<li><a href="#">Photography</a></li>\
					</ul>\
			 	</li>\
			 </ul>\
        </div>         \
         </div>')
	// $("#params").append()

	var slider = document.getElementById('slider');

	noUiSlider.create(slider, {
		start: [0, 5000],
		connect: true,
		range: {
			'min': 0,
			'max': 50000,
		},
		pips: { 
			mode: 'count',
			values: 6,
			density: 4

		},
		// format: wNumb({
		// 	decimals: 3,
		// 	thousand: '.',
		// 	postfix: ' (US $)',
		// })
	});
	slider.noUiSlider.on("change", change_price)

	// $("#params").append('<div style="margin:10px;width:100%;height:3%"> <input type="range" id="price_input" class="floatLeft edit_border" min="0" max="50000" step="1" value="25000"  style="width:50%;" oninput="change_price();"><h3 style="text-align:center">Ценовая категория <p id="price">10050</p></h3></div>')
 });