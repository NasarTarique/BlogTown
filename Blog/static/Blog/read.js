window.addEventListener('DOMContentLoaded', ()=>{
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
});


