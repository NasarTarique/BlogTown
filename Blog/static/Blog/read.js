document.addEventListener('DOMContentLoaded', ()=>{
		let postcards = document.querySelectorAll('.post-card')
		let lefticon = document.querySelector('.left-icon')
		let righticon = document.querySelector('.right-icon')
		let firstpost = 0
		let lastpost = 3
		

		for(let i=0;i<4;i++){
				postcards[i].style.display = "block"
		}

		lefticon.addEventListener("click", ()=>{
				let p = firstpost
				if(p > 0){
						postcards[lastpost].style.display = "none"
						firstpost = firstpost - 1
						lastpost = lastpost - 1
						postcards[firstpost].style.display = "block"
				}
		})

		righticon.addEventListener('click', ()=>{
				let post = lastpost 
				if(postcards.length > (post+1)){
					postcards[firstpost].style.display = "none";
					lastpost  = lastpost+1
					firstpost = firstpost + 1 
					postcards[lastpost].style.display = "block"

				}
		})
		postcards.forEach((element) => {
				element.addEventListener("click", ()=>{
						let url = element.dataset.url 
						window.location.href = url
				})
		})

		var queries = [
				window.matchMedia("(min-width:1450px)"),
				window.matchMedia("(max-width:1450px) and (min-width:900px)"),
				window.matchMedia("(max-width:900px) and (min-width:600px)"),
				window.matchMedia("(max-width:600px)")
//				window.matchMedia("()"),
//				window.matchMedia("()"),
//				window.matchMedia("()"),
//				window.matchMedia("()"),
		]
		function mqs(mq){
				let allpost = lastpost -firstpost + 1;
				if(queries[0].matches){
						if(allpost<4){
								lastpost++;
								postcards[lastpost].style.display = "block";
						}

				}
				if(queries[1].matches ){
						console.log("hello ");
						if(allpost===4){
								postcards[lastpost].style.display = "none"
								lastpost--;
						}
						else if(allpost<3){
								lastpost++;
								postcards[lastpost].style.display = "block";
						}
				}
				if(queries[2].matches){
						if(allpost>2){
								while(allpost!=2){
								postcards[lastpost].style.display = "none"
								lastpost = lastpost -1;
						        allpost--;
								}
						}
						else if(allpost<2){
								lastpost++;
								postcards[lastpost].style.display = "block";
						}
				}
				if(queries[3].matches){
								while(allpost!=1){
								postcards[lastpost].style.display = "none"
								lastpost = lastpost -1;
						        allpost--;
								}
				}
		}

		for(let i=0;i<queries.length; i++)	{
				console.log("hello");
				mqs(queries[i]);
				queries[i].addListener(mqs);

		}

});
