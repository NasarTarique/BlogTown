document.addEventListener("DOMContentLoaded", () => {
  let obs = document.querySelector(".observer");
  let g1 = document.querySelector(".grid-1");
  let pg = 3;
  let uri = "http://127.0.0.1:8000/Blog/post";
  let g1complete = false;

  let options = {
    threshold: 0.1,
  };


  function fetchposts(page) {
		  let url1 = uri + "?page=" + page + "&genre="+obs.dataset.genre;
      fetch(url1)
        .then((resp) => {
          if (resp.ok) {
            return resp.text();
          } else return "error404";
        })
        .then((data) => {
          if (data === "error404") {
            g1complete = true;
          } else {
            g1.innerHTML += data;
          }
        })
		.then(() => {})
  }
		

  let observer = new IntersectionObserver(function (entries) {
    if (entries[0].intersectionRatio > 0) {
      fetchposts(pg);
      pg++;
    }
    if (g1complete) {
      observer.unobserve(obs);
    }
  }, options);


  observer.observe(obs);
});
