// <!-- Start Password Strength -->
const pw = document.getElementById('password'),
 eyeicon = document.getElementById('eye'),
 	psbg = document.querySelector('.psbg'),
   login = document.getElementById('login'),
   email = document.getElementById('email'),
   	 wdf = document.querySelector('.wdf'),
  psform = document.querySelector('.psform');


eyeicon.addEventListener('click',()=>{
	// console.log('hey');

	if(eyeicon.classList.contains('fa-eye')){

		eyeicon.classList.replace('fa-eye','fa-eye-slash');
		pw.setAttribute('type','text');

	}else{

		eyeicon.classList.replace('fa-eye-slash','fa-eye');
		pw.setAttribute('type','password');

	}

});


pw.addEventListener('input',(e)=>{
	// console.log(pw.value);

	const pwvalue = e.target.value;
	const blurvalue = 10 - pwvalue.length;

	psbg.style.filter = `blur(${blurvalue}px)`;

});


login.addEventListener('click',(e)=>{
	// console.log('login');

	if(pw.value === '0123456789' && email.value === 'user@gmail.com'){

		// console.log('success');
		e.preventDefault();

		wdf.classList.add('disappear');
		psform.classList.add('disappear');

		// console.log(wdf);
		// console.log(psform);

		if(wdf.classList.contains('disappear')){

			wdf.style.display = 'none';
		}

		if(psform.classList.contains('disappear')){

			psform.style.display = 'none';
		}

		

	}else{

		window.alert('Enter the correct account to login ! Try Again.');
	}

});
// <!-- End Password Strength -->



// <!-- Start Net -->
const togglerbtn = document.querySelector('.toggler-btn'),
		 	navs = document.querySelectorAll('.nav');


togglerbtn.addEventListener('click',()=>{
	// console.log('hey');

	navs.forEach(nav=>nav.classList.toggle('visible'));

	// console.log(navs);

});
// <!-- End Net -->



// <!-- Start Stop Watch -->
const display = document.getElementById('display'),
	 startbtn = document.getElementById('start'),
	 pausebtn = document.getElementById('pause'),
	 resetbtn = document.getElementById('reset'),
	stopwatch = document.querySelector('.stopwatch'),
	  swclose = document.querySelector('.closebtn'),
  swcontainer = document.querySelector('.stopwatch-container');

stopwatch.addEventListener('click',()=> swcontainer.classList.toggle('visible'));

swclose.addEventListener('click',()=> swcontainer.classList.remove('visible'));

// console.log(display);
// console.log(startbtn);
// console.log(pausebtn);
// console.log(resetbtn);

let [milisec,sec,min,hr] = [0,0,0,0];
let time;

startbtn.addEventListener('click',starttime);
pausebtn.addEventListener('click',pausetime);
resetbtn.addEventListener('click',resettime);

function displaytime(){

	milisec += 10;

	if(milisec === 1000){
		milisec = 0;

		sec ++;

		if(sec === 60){

			sec = 0;

			min ++;

			if(min === 60){

				hr ++;
			}
		}
	}

	let h = hr < 10 ? "0"+hr : hr;
	let m = min < 10 ? "0"+min : min;
	let s = sec < 10 ? "0"+sec : sec;
	let ms = milisec < 10 ? "00"+milisec : milisec < 100 ? "0"+milisec : milisec;

	display.innerText = `${h} : ${m} : ${s} : ${ms}`;

}

function starttime(){

	if(time != null){
		clearInterval(time);
	}

	time = setInterval(displaytime,10);

}

function pausetime(){

	clearInterval(time);
}

function resettime(){

	clearInterval(time);

	[milliseconds,seconds,minutes,hours] = [0,0,0,0];

	display.innerText = "00 : 00 : 00 : 000";
}
// <!-- End Stop Watch -->



// <!-- Start Todo List -->
const formelement = document.querySelector('.orderinput'),
	   orderinput = document.getElementById('order'),
	      orderul = document.getElementById('orderlist'),
	         todo = document.querySelector('.todo'),
	     todolist = document.getElementById('todolist'),
	   orderclose = document.getElementById('orderclosebtn');

todo.addEventListener('click', ()=> todolist.classList.toggle('visible'));

orderclose.addEventListener('click', ()=> todolist.classList.remove('visible'));


const orders = JSON.parse(localStorage.getItem('totalorder'));
		
if(orders){
	orders.forEach(order => addtoorder(order));
}

formelement.addEventListener('submit',(e)=>{
 
  addtoorder();

  e.preventDefault();

});

function addtoorder(order){

	let ordertext = orderinput.value;

	if(order){
		ordertext = order.text;
	}

	if(ordertext){

		const li = document.createElement('li');

		if(order && order.completed){
			li.classList.add('completed');
		}

		li.appendChild(document.createTextNode(ordertext));

		orderul.appendChild(li);

		orderinput.value = '';

		updatelocalstorage();


		li.addEventListener('click',()=>{

			li.classList.toggle('completed');

			updatelocalstorage();

		});

		li.addEventListener('contextmenu',(e)=>{

			li.remove();

			updatelocalstorage();

			e.preventDefault();

		});

	}

}

function updatelocalstorage(){

	const orderlis = document.querySelectorAll('li');

	const lis = [];

	orderlis.forEach(orderli => {

		lis.push( { text : orderli.ordertext , completed : orderli.classList.contains('completed') } );

	});

	localStorage.setItem('totalorder',JSON.stringify(lis));

}
// <!-- End Todo List -->



// <!-- Start Pricing Section -->

// <!-- End Pricing Section -->



// <!-- Start Toast Notification -->

// <!-- End Toast Notification -->