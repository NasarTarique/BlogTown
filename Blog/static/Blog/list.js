document.addEventListener("DOMContentLoaded", () => {
  let obs = document.querySelector(".observer");
  let g1 = document.querySelector(".grid-1");
  let g2 = document.querySelector(".grid-2");
  let pg = 2;
  let uri = "http://127.0.0.1:8000/Blog/post";
		let g1complete = false ;
		let g2complete = false ;

  let options = {
    threshold: 0.1,
  };

  function fetchposts(page) {
    let url1 = uri + "?page=" + page + "&grid=1";
    let url2 = uri + "?page=" + page + "&grid=2";


    Promise.all([
      fetch(url1)
			.then((resp) => {
					if(resp.ok){
							return resp.text()

					}
					else
							return "error404"
			})
			.then((data) => {
					console.log(data)
					if(data === "error404"){
							g1complete == true

					}else{
							g1.innerHTML += data
					}
			})
			.then(()=>{
			}),


		
			fetch(url2)
			.then(resp => {
					if(resp.ok){
							return resp.text()
					}
					else{
							return "error404"
					}
			})
			.then(data =>{
					if(!(data === "error404")){
							g2.innerHTML +=data
					}
					else{
						g2complete = true	
					}
			})
    ]);
  }
  let observer = new IntersectionObserver(function (entries) {
		  if(entries[0].intersectionRatio > 0){
    			fetchposts(pg);
    			pg++;
		  }
		  if(g1complete && g2complete ){
				  observer.unobserve(obs)
				  console.log("true");
		  }
  },options);
  observer.observe(obs);
});
