// UI
const form = document.getElementById("form");
const username = document.getElementById("username");
const email = document.getElementById("email");
const password = document.getElementById("password");
const cfnpassword = document.getElementById("cfnpassword");


// Event Listener (Method 1)
// form.addEventListener('submit',function(e){

// 	e.preventDefault();
// 	//console.log("hey");

// 	//username
// 	if(username.value === ''){

// 		showerror(username,"Username is required.");

// 	}else{
// 		showsuccess(username);
// 	}


// 	//email
// 	if(email.value === ''){

// 		showerror(email,"Email is required.");

// 	}else if(!validateEmail(email.value)){

// 		showerror(email,"Email is not valid.");

// 	}else{
// 		showsuccess(email);
// 	}


// 	//password
// 	if(password.value === ''){

// 		showerror(password,"Passowrd is required.");

// 	}else{
// 		showsuccess(password);
// 	}



// 	//confirm password
// 	if(cfnpassword.value === ''){

// 		showerror(cfnpassword,"Confirm passowrd is required.");

// 	}else if(password.value !== cfnpassword.value){

// 		showerror(cfnpassword,"Passowrds do not match.");

// 	}else{
// 		showsuccess(cfnpassword);
// 	}
// });


function showerror(input,message){

	const formcontrol = input.parentElement;
	formcontrol.className = "form-control error";

	//document loh ma pay pl formcontrol loh pay mha
	const small = formcontrol.querySelector("small");
	small.innerText = message;

}

function showsuccess(input){

	const formcontrol = input.parentElement;

	formcontrol.className = "form-control success";
	// formcontrol.classList.remove("error");
	// formcontrol.classList.add("success");
}


//For checking email format
//regular expression
// function validateEmail(email) {
//     const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
//     return re.test(String(email).toLowerCase());
// }


// Check Required Field
function checkrequired(inputarr){

	// console.log(inputarr);

	inputarr.forEach(function(input){

		// console.log(input);
		// console.log(input.value);
		// console.log(input.id);


		if(input.value === ''){

			showerror(input,`${getfieldname(input)} is required.`);

		}else{

			showsuccess(input);
		}

	});

}



// Get Field Name
function getfieldname(input){

	return input.id.charAt(0).toUpperCase() + input.id.slice(1);
}


// Check Input Length
function checklength(input,min,max){

	if(input.value.length < min){

		showerror(input,`${getfieldname(input)} must be at least ${min} characters.`);

	}else if(input.value.length > max){

		showerror(input,`${getfieldname(input)} must be less than ${max} characters.`);
	}else{

		showsuccess(input);
	}
}


// Check Email is valid
function checkemail(input){

	const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    //return re.test(String(email).toLowerCase());

    if(re.test(input.value)){

    	showsuccess(input);
    }else{

    	showerror(input,"Email is not valid.");
    }
}


// Check Password Match
function checkpasswordsmatch(input1,input2){

	if(input1.value !== input2.value){

		showerror(input2,"Password do not match.");
	}
}




// Event Listener (Method 2)
form.addEventListener("submit",function(e){
	e.preventDefault();
	// console.log("hey");

	checkrequired([username,email,password,cfnpassword]);


	checklength(username,3,15);
	checklength(password,6,25);

	checkemail(email);

	checkpasswordsmatch(password,cfnpassword);

});