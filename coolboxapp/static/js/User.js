$(document).ready(function(){
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();
	
	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;                        
			});
		} else{
			checkbox.each(function(){
				this.checked = false;                        
			});
		} 
	});
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
});

$(document).ready(function(){
	// Activate tooltips
	$('[data-toggle="tooltip"]').tooltip();
    
	// Filter table rows based on searched term
    $("#search").on("keyup", function() {
        var term = $(this).val().toLowerCase();
        $("table tbody tr").each(function(){
            $row = $(this);
            var name = $row.find("td:nth-child(2)").text().toLowerCase();
            console.log(name);
            if(name.search(term) < 0){                
                $row.hide();
            } else{
                $row.show();
            }
        });
    });
});

/*==================== SHOW NAVBAR ====================*/
const showMenu = (headerToggle, navbarId) =>{
	const toggleBtn = document.getElementById(headerToggle),
	nav = document.getElementById(navbarId)
	
	// Validate that variables exist
	if(headerToggle && navbarId){
		toggleBtn.addEventListener('click', ()=>{
			// We add the show-menu class to the div tag with the nav__menu class
			nav.classList.toggle('show-menu')
			// change icon
			toggleBtn.classList.toggle('bx-x')
		})
	}
  }
  showMenu('header-toggle','navbar')
  
  /*==================== LINK ACTIVE ====================*/
  const linkColor = document.querySelectorAll('.nav__link')
  
  function colorLink(){
	linkColor.forEach(l => l.classList.remove('active'))
	this.classList.add('active')
  }
  
  linkColor.forEach(l => l.addEventListener('click', colorLink))
  
  /*==================== Check con ====================*/
  function checkPasswordb(form) { 
	var password = document.getElementById("password").value;
	var cPassword = document.getElementById("confirm_password").value;
	if (password == '') {
		  alert ("Please enter Password")
	  return false; 
	}			
		  // ถ้าช่่องยืนยันรหัสผ่านไม่ถูกกรอก
	  else if (cPassword == '') {
		  alert ("Please enter confirm password"); 
	  return false;
	}
  
	else if (password != cPassword) { 
	  alert ("\nPassword did not match: Please try again...") 
	  return false; 
	  } 
  
	//ถ้าทั้งสองช่องตรงกัน  return true
	else if (confirm("ต้องการบันทึกข้อมูลหรือไม่?")){
	  return true;   
	}
	else{ 
  
	  return false;
   
	  } 
  } 
  
  