function  isempty(tag){
		if(tag.value === null || tag.value === undefined || tag.value === ''){
				tag.style.color = '#FF4949'
				tag.placeholder = 'Required'
				return false;
		}else{
				return true;
		}
}

document.addEventListener('DOMContentLoaded',()=>{
		
		let method  = document.querySelector('.container').dataset.method;

		if( method === 'get' ){

		let contactname = document.querySelector('#name-input')
		let contactmail = document.querySelector("#mail-input")	
		let mailcontent = document.querySelector("#textarea") 
		
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

		document.querySelector(".form-submit").addEventListener('click',()=>{
				if(isempty(contactname) && isempty(contactmail) && isempty(mailcontent)){
												document.querySelector('form').submit()
				}else{
						isempty(contactmail)
						isempty(mailcontent)
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
