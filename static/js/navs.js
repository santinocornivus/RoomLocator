const navbar = document.querySelector('.nav_bar')
		const menu = document.querySelector('.menu_list');
		const  menuBtn = document.querySelector('.menu_btn');
		const cancelBtn = document.querySelector('.cancel_btn');

		menuBtn.onclick = () =>{
			menu.classList.add('active')
			menuBtn.classList.add('hide')
		}

		cancelBtn.onclick = () =>{
			menu.classList.remove('active')
			menuBtn.classList.remove('hide')
		}

		window.onscroll = () => {
			this.scrollY > 20 ? navbar.classList.add('sticky') : navbar.classList.remove('sticky');
		}