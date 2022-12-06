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
function popup(form) { 
    if (confirm("ต้องการบันทึกข้อมูลหรือไม่?")){
        return true;   
    }
    else{ 

        return false;
     
        } 
} 


// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
