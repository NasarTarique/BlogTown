window.addEventListener('DOMContentLoaded', ()=>{
		let postcards = document.querySelectorAll('.post-card')
		postcards.forEach((element) => {
				element.addEventListener("click", ()=>{
						let url = window.location.href.slice(0,-1) + element.dataset.number
						window.location.href = url
				})
		})
});
