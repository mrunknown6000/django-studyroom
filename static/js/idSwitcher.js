
function switchID(id, range){
	// Clicked ID
	document.getElementById(id).classList.add('text-blue-400 border-b-2 border-blue-600')
	document.getElementById(id).classList.remove('unactive')
	console.log('triggered')
	console.log(id)
	console.log(range)
	for (var i = 0; i < range; i++) {
		if (i == id){
			continue;
		}
		document.getElementById(i).classList.remove('text-blue-400 border-b-2 border-blue-600')
		document.getElementById(i).classList.add('unactive')
	}
}