window.onscroll = function() {stickyNav()};

var navbarVar = document.getElementById("navbarTrue");

var stickyNav = navbarVar.offsetTop;

function stickyNav(){
	if (window.pageYOffset >= stickyNav){
		navbarVar.classList.add("navbar-sticky");
	} else {
		navbarVar.classList.remove("navbar-sticky");
	}
}

// Sidebar
function closeNav() {
	document.getElementById('sidebar').style.width = "0rem";
}

function openNav() {
	document.getElementById('sidebar').style.width = "20vh";
}
