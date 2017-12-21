

/* checks if login is valid*/
function login(form) {
	var answer = "username";
	if (form.user.value==answer) {
		if (form.pwd.value=="password") {
			location="account.html"
		} else {
			alert("Invalid Password")
		}
	} else { alert("Invalid UserID")
	}
}

function getCookie(c_name) {
	if (document.cookie.length > 0) {
		c_start = document.cookie.indexOf(c_name + "=");
		if (c_start != -1) {
			c_start = c_start + c_name.length + 1;
			c_end = document.cookie.indexOf(";", c_start);
			if (c_end == -1) {
					c_end = document.cookie.length;
			}
		return unescape(document.cookie.substring(c_start, c_end));
		}
	}
	return "";
}

/*Allows a person to leave a comment*/
function comment(){
	/*Gets the name entered in the form*/
	var name = document.getElementById('name').value;
	/*gets dat*/
	var d = new Date();
	var month = d.getUTCMonth() + 1;
	var day = d.getUTCDate();
	var year = d.getUTCFullYear();
	today = day+ "/" + month + "/" + year;
	/*gets comment entered in the form*/
	var comment = document.getElementById('com').value;
	/* Checks if the radio boxes are checked and gives the variable rate the number of the box that is checked */
	var rate1 = document.getElementById('radio1').checked;
	var rate2 = document.getElementById('radio2').checked;
	var rate3 = document.getElementById('radio3').checked;
	var rate4 = document.getElementById('radio4').checked;
	var rate5 = document.getElementById('radio5').checked;
	var rate;
	if(rate1){
		rate = 1;
	} else if(rate2){
		rate = 2;
	} else if(rate3){
		rate = 3;
	} else if(rate4){
		rate = 4;
	} else {
		rate = 5;
	}
	/* adds the code with the comment */
	document.getElementById('comments').innerHTML =  '<div class="media"><div class="media-left"><img src="images/avatar.png" class="media-object" style="width:45px"></div><div class="media-body">' +
	' <h4 class="media-heading">' + name + '<small><i>Posted on ' + today + '</i></small></h4>' +
	'<div class="rating2">' +
	'<button type="submit" class="star starRVW" id="1005a" ><span class="glyphicon glyphicon-star" id="star1005a"></span></button>' +
	'<button type="submit" class="star starRVW" id="1005b" ><span class="glyphicon glyphicon-star" id="star1005b"></span></button>' +
	'<button type="submit" class="star starRVW" id="1005c" ><span class="glyphicon glyphicon-star" id="star1005c"></span></button>' +
	'<button type="submit" class="star starRVW" id="1005d" ><span class="glyphicon glyphicon-star" id="star1005d"></span></button>' +
	'<button type="submit" class="star starRVW" id="1005e" ><span class="glyphicon glyphicon-star" id="star1005e"></span></button>' +
	'</div><p>'+ comment  + '</p></div></div>';
	/*calls function reviewed*/
	reviewed("1005", rate);
}

/* changes color of the heart into red when pressed */
function liked(Id){
		document.getElementById(Id).style.color = "Red";
		document.cookie = Id + "="  + 1;
}
/*Gets the rating the users have given them and colors the starts red accordingly*/
function userRated(id, st){
	a = "star" + id + "a";
	b = "star" + id + "b";
	c = "star" + id + "c";
	d = "star" + id + "d";
	e = "star" + id + "e";
	var star = st;

	var name = "pk" + id;
	document.cookie = name + "="  + star;

	if(star == 1){
		document.getElementById(a).style.color = "#ffcc00";
		document.getElementById(b).style.color = "#cccccc";
		document.getElementById(c).style.color = "#cccccc";
		document.getElementById(d).style.color = "#cccccc";
		document.getElementById(e).style.color = "#cccccc";
	} else if(star == 2){
		document.getElementById(a).style.color = "#ffcc00";
		document.getElementById(b).style.color = "#ffcc00";
		document.getElementById(c).style.color = "#cccccc";
		document.getElementById(d).style.color = "#cccccc";
		document.getElementById(e).style.color = "#cccccc";
	} else if(star == 3){
		document.getElementById(a).style.color = "#ffcc00";
		document.getElementById(b).style.color = "#ffcc00";
		document.getElementById(c).style.color = "#ffcc00";
		document.getElementById(d).style.color = "#cccccc";
		document.getElementById(e).style.color = "#cccccc";
	} else if(star == 4){
		document.getElementById(a).style.color = "#ffcc00";
		document.getElementById(b).style.color = "#ffcc00";
		document.getElementById(c).style.color = "#ffcc00";
		document.getElementById(d).style.color = "#ffcc00";
		document.getElementById(e).style.color = "#cccccc";
	}  else if(star==5){
		document.getElementById(a).style.color = "#ffcc00";
		document.getElementById(b).style.color = "#ffcc00";
		document.getElementById(c).style.color = "#ffcc00";
		document.getElementById(d).style.color = "#ffcc00";
		document.getElementById(e).style.color = "#ffcc00";
	} else{
		document.getElementById(a).style.color = "#cccccc";
		document.getElementById(b).style.color = "#cccccc";
		document.getElementById(c).style.color = "#cccccc";
		document.getElementById(d).style.color = "#cccccc";
		document.getElementById(e).style.color = "#cccccc";
	}
}

/*allows the user to leave a reating and colors the start yellow accordingly*/
function rated(id, st){
	a = "star" + id + "a";
	b = "star" + id + "b";
	c = "star" + id + "c";
	d = "star" + id + "d";
	e = "star" + id + "e";
	var star = st;
	if(star == 1){
		document.getElementById(a).style.color = "#ff3300";
		document.getElementById(b).style.color = "#cccccc";
		document.getElementById(c).style.color = "#cccccc";
		document.getElementById(d).style.color = "#cccccc";
		document.getElementById(e).style.color = "#cccccc";
	} else if(star == 2){9
		document.getElementById(a).style.color = "#ff3300";
		document.getElementById(b).style.color = "#ff3300";
		document.getElementById(c).style.color = "#cccccc";
		document.getElementById(d).style.color = "#cccccc";
		document.getElementById(e).style.color = "#cccccc";
	} else if(star == 3){
		document.getElementById(a).style.color = "#ff3300";
		document.getElementById(b).style.color = "#ff3300";
		document.getElementById(c).style.color = "#ff3300";
		document.getElementById(d).style.color = "#cccccc";
		document.getElementById(e).style.color = "#cccccc";
	} else if(star == 4){
		document.getElementById(a).style.color = "#ff3300";
		document.getElementById(b).style.color = "#ff3300";
		document.getElementById(c).style.color = "#ff3300";
		document.getElementById(d).style.color = "#ff3300";
		document.getElementById(e).style.color = "#cccccc";
	}  else if(star==5){
		document.getElementById(a).style.color = "#ff3300";
		document.getElementById(b).style.color = "#ff3300";
		document.getElementById(c).style.color = "#ff3300";
		document.getElementById(d).style.color = "#ff3300";
		document.getElementById(e).style.color = "#ff3300";
	} else{
		document.getElementById(a).style.color = "#cccccc";
		document.getElementById(b).style.color = "#cccccc";
		document.getElementById(c).style.color = "#cccccc";
		document.getElementById(d).style.color = "#cccccc";
		document.getElementById(e).style.color = "#cccccc";
	}
}

/* Shows the rating that have been given in reviews*/
function reviewed(id, st){
	a = "star" + id + "a";
	b = "star" + id + "b";
	c = "star" + id + "c";
	d = "star" + id + "d";
	e = "star" + id + "e";
	var star = st;

	if(star == 1){
		document.getElementById(a).style.color = "#ffcc00";
		document.getElementById(b).style.color = "#cccccc";
		document.getElementById(c).style.color = "#cccccc";
		document.getElementById(d).style.color = "#cccccc";
		document.getElementById(e).style.color = "#cccccc";
	} else if(star == 2){
		document.getElementById(a).style.color = "#ffcc00";
		document.getElementById(b).style.color = "#ffcc00";
		document.getElementById(c).style.color = "#cccccc";
		document.getElementById(d).style.color = "#cccccc";
		document.getElementById(e).style.color = "#cccccc";
	} else if(star == 3){
		document.getElementById(a).style.color = "#ffcc00";
		document.getElementById(b).style.color = "#ffcc00";
		document.getElementById(c).style.color = "#ffcc00";
		document.getElementById(d).style.color = "#cccccc";
		document.getElementById(e).style.color = "#cccccc";
	} else if(star == 4){
		document.getElementById(a).style.color = "#ffcc00";
		document.getElementById(b).style.color = "#ffcc00";
		document.getElementById(c).style.color = "#ffcc00";
		document.getElementById(d).style.color = "#ffcc00";
		document.getElementById(e).style.color = "#cccccc";
	} else if(star==5){
		document.getElementById(a).style.color = "#ffcc00";
		document.getElementById(b).style.color = "#ffcc00";
		document.getElementById(c).style.color = "#ffcc00";
		document.getElementById(d).style.color = "#ffcc00";
		document.getElementById(e).style.color = "#ffcc00";
	} else{
		document.getElementById(a).style.color = "#cccccc";
		document.getElementById(b).style.color = "#cccccc";
		document.getElementById(c).style.color = "#cccccc";
		document.getElementById(d).style.color = "#cccccc";
		document.getElementById(e).style.color = "#cccccc";
	}
}
