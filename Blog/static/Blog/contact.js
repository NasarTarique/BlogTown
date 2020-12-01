function  notempty(tag){
		if(tag.value === null || tag.value === undefined || tag.value === ''){
				tag.style.color = '#FF4949'
				tag.placeholder = 'Required'
				return false;
		}else{
				return true;
		}
}

document.addEventListener('DOMContentLoaded',()=>{
		
		let method  = document.querySelector('.contact').dataset.method;

		if( method === 'get' ){

		let contactname = document.querySelector('#name-input')
		let contactmail = document.querySelector("#mail-input")	
		let mailcontent = document.querySelector("#message") 
		
		contactmail.addEventListener('click', ()=>{
				if(contactmail.placeholder != ''){
						contactmail.placeholder = ''
						contactmail.style.color = '#50D894'
				}
		})

		contactname.addEventListener('click', ()=>{
				if(contactname.placeholder != ''){
						contactname.placeholder = ''
						contactname.style.color = '#50D894'
				}
		})

		mailcontent.addEventListener('click', ()=>{
				if(mailcontent.placeholder != ''){
						mailcontent.placeholder = ''
						mailcontent.style.color = '#50D894'
				}
		})

		document.querySelector(".submit-button").addEventListener('click',()=>{
				console.log('yo')
				if(notempty(contactname) && notempty(contactmail) && notempty(mailcontent)){
												document.querySelector('form').submit()
				}else{
						notempty(contactmail)
						notempty(mailcontent)
				}

		})



		}
		else if(method === 'post'){
				document.querySelector('.back-button').addEventListener('click', ()=>{
						let url = window.location.href
						console.log('href')
						window.location.assign(url)
				})
		}
		

})
