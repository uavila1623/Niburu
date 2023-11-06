// Updated County Javascript autocomplete file
var counties = ['Accomack', 'Ada', 'Adair', 'Adams', 'Addison', 'Aiken', 'Aitkin', 'Alachua', 'Alamance', 'Alameda', 'Alamosa', 'Albany', 'Albemarle', 'Alcorn', 'Alexander', 'Alger', 'Allegan', 'Allegany', 'Allegheny', 'Allen', 'Alpena', 'Anderson', 'Andrews', 'Androscoggin', 'Angelina', 'Anne Arundel', 'Anoka', 'Anson', 'Antrim', 'Apache', 'Appanoose', 'Aransas', 'Arapahoe', 'Archuleta', 'Arlington', 'Aroostook', 'Ascension', 'Ashe', 'Ashland', 'Ashtabula', 'Atascosa', 'Athens', 'Atlantic', 'Atoka', 'Audubon', 'Augusta', 'Baca', 'Bacon', 'Baker', 'Baldwin', 'Baltimore City', 'Baltimore County', 'Barber', 'Barbour', 'Barnes', 'Barnstable', 'Barnwell', 'Barren', 'Barron', 'Barrow', 'Barry', 'Bartholomew', 'Barton', 'Bartow', 'Bath', 'Baxter', 'Bay', 'Beadle', 'Beaufort', 'Beauregard', 'Beaver', 'Beaverhead', 'Becker', 'Bedford', 'Bee', 'Belknap', 'Bell', 'Beltrami', 'Ben Hill', 'Bennington', 'Benton', 'Benzie', 'Bergen', 'Berkeley', 'Berks', 'Berkshire', 'Bernalillo', 'Berrien', 'Bexar', 'Big Horn', 'Big Stone', 'Black Hawk', 'Bladen', 'Blaine', 'Blair', 'Blount', 'Blue Earth', 'Bolivar', 'Bonner', 'Bonneville', 'Boone', 'Bossier', 'Boulder', 'Boundary', 'Bourbon', 'Bowman', 'Box Butte', 'Box Elder', 'Bradley', 'Branch', 'Braxton', 'Brazoria', 'Brazos', 'Breathitt', 'Brevard', 'Brewster', 'Bristol', 'Brookings', 'Brooks', 'Broome', 'Broward', 'Brown', 'Brule', 'Brunswick', 'Bryan', 'Buchanan', 'Bucks', 'Buena Vista', 'Buffalo', 'Bulloch', 'Buncombe', 'Burke', 'Burleigh', 'Burleson', 'Burlington', 'Burnet', 'Burnett', 'Burt', 'Butler', 'Butte', 'Cabarrus', 'Cache', 'Caddo', 'Calcasieu', 'Caldwell', 'Caledonia', 'Calhoun', 'Callaway', 'Calloway', 'Cambria', 'Camden', 'Cameron', 'Campbell', 'Canadian', 'Canyon', 'Cape May', 'Carbon', 'Caribou', 'Carlton', 'Caroline', 'Carroll', 'Carson City', 'Carter', 'Carteret', 'Cascade', 'Cass', 'Cassia', 'Catawba', 'Cattaraugus', 'Cavalier', 'Centre', 'Cerro Gordo', 'Chaffee', 'Champaign', 'Charleston', 'Charlevoix', 'Charlotte', 'Chase', 'Chatham', 'Chattahoochee', 'Chautauqua', 'Chaves', 'Cheboygan', 'Chemung', 'Cherokee', 'Cherry', 'Chesapeake', 'Cheshire', 'Chester', 'Chesterfield', 'Cheyenne', 'Childress', 'Chippewa', 'Chisago', 'Chittenden', 'Choctaw', 'Chowan', 'Christian', 'Churchill', 'Cibola', 'Citrus', 'Clallam', 'Clarendon', 'Clark', 'Clarke', 'Clatsop', 'Clay', 'Clayton', 'Clearfield', 'Clermont', 'Cleveland', 'Clinch', 'Clinton', 'Cloud', 'Coahoma', 'Cobb', 'Cochise', 'Coconino', 'Codington', 'Coffee', 'Coffey', 'Colbert', 'Coleman', 'Coles', 'Colfax', 'Colleton', 'Collier', 'Collin', 'Colquitt', 'Columbia', 'Columbus', 'Comanche', 'Conecuh', 'Contra Costa', 'Converse', 'Cook', 'Cooke', 'Cooper', 'Coos', 'Cortland', 'Coryell', 'Costilla', 'Cottonwood', 'Covington', 'Coweta', 'Cowley', 'Cowlitz', 'Craighead', 'Craven', 'Crawford', 'Crisp', 'Crittenden', 'Crockett', 'Crook', 'Crow Wing', 'Culberson', 'Cullman', 'Culpeper', 'Cumberland', 'Currituck', 'Curry', 'Custer', 'Cuyahoga', 'Dakota', 'Dale', 'Dallas', 'Dane', 'Danville', 'Dare', 'Darke', 'Darlington', 'Dauphin', 'Davidson', 'Daviess', 'Davis', 'Davison', 'Dawes', 'Dawson', 'DeKalb', 'DeSoto', 'Deaf Smith', 'Decatur', 'Defiance', 'Del Norte', 'Delaware', 'Delta', 'Denton', 'Denver', 'Des Moines', 'Deschutes', 'Dickey', 'Dickinson', 'Dinwiddie', 'Divide', 'Dixie', 'Dodge', 'Door', 'Dorchester', 'Dougherty', 'Douglas', 'Doña Ana', 'Drew', 'DuPage', 'Dubois', 'Dubuque', 'Dukes', 'Dunn', 'Duplin', 'Dutchess', 'Duval', 'Dyer', 'Eagle', 'Early', 'East Baton Rouge', 'Eaton', 'Ector', 'Eddy', 'Edgar', 'Edgecombe', 'Edwards', 'Effingham', 'El Dorado', 'El Paso', 'Elbert', 'Elkhart', 'Elko', 'Ellis', 'Elmore', 'Emanuel', 'Emery', 'Emmet', 'Emmons', 'Erath', 'Erie', 'Escambia', 'Essex', 'Etowah', 'Eureka', 'Evans', 'Fairfax County', 'Fairfield', 'Fallon', 'Fauquier', 'Fayette', 'Fergus', 'Fillmore', 'Finney', 'Flagler', 'Flathead', 'Florence', 'Floyd', 'Fond du Lac', 'Ford', 'Forrest', 'Forsyth', 'Fort Bend', 'Foster', 'Franklin', 'Frederick', 'Freeborn', 'Fremont', 'Fresno', 'Fulton', 'Gadsden', 'Gage', 'Gaines', 'Gallatin', 'Galveston', 'Garfield', 'Garland', 'Garrett', 'Garvin', 'Gaston', 'Geary', 'Genesee', 'Georgetown', 'Gila', 'Gillespie', 'Glacier', 'Glynn', 'Gogebic', 'Golden Valley', 'Gonzales', 'Goodhue', 'Goshen', 'Grady', 'Grafton', 'Graham', 'Grand', 'Grand Forks', 'Grand Traverse', 'Granite', 'Grant', 'Granville', 'Gratiot', 'Graves', 'Gray', 'Grays Harbor', 'Grayson', 'Green', 'Greenbrier', 'Greene', 'Greensville', 'Greenville', 'Greenwood', 'Gregg', 'Griggs', 'Grundy', 'Guadalupe', 'Guilford', 'Gunnison', 'Gwinnett', 'Haakon', 'Hale', 'Halifax', 'Hall', 'Hamilton', 'Hampden', 'Hampton', 'Hancock', 'Hanover', 'Hardin', 'Harding', 'Harford', 'Harlan', 'Harnett', 'Harney', 'Harris', 'Harrison', 'Hartford', 'Hartley', 'Harvey', 'Haskell', 'Hemphill', 'Henderson', 'Hennepin', 'Henrico', 'Henry', 'Hernando', 'Hertford', 'Hidalgo', 'Hill', 'Hillsborough', 'Hillsdale', 'Hinds', 'Holmes', 'Holt', 'Hood', 'Hood River', 'Hopkins', 'Horry', 'Hot Springs', 'Houghton', 'Houston', 'Howard', 'Howell', 'Hubbard', 'Hughes', 'Humboldt', 'Hunt', 'Huron', 'Hutchinson', 'Hyde', 'Iberia', 'Idaho', 'Imperial', 'Independence', 'Indian River', 'Indiana', 'Ingham', 'Inyo', 'Ionia', 'Iosco', 'Iowa', 'Iredell', 'Iron', 'Isabella', 'Isanti', 'Island', 'Isle of Wight', 'Itasca', 'Jackson', 'James City', 'Jasper', 'Jeff Davis', 'Jefferson', 'Jefferson Davis', 'Jerome', 'Jim Hogg', 'Jim Wells', 'Johnson', 'Johnston', 'Jones', 'Josephine', 'Juneau', 'Kalamazoo', 'Kanabec', 'Kanawha', 'Kandiyohi', 'Kane', 'Kankakee', 'Kaufman', 'Kay', 'Keith', 'Kennebec', 'Kenosha', 'Kent', 'Kern', 'Kerr', 'Kershaw', 'Keweenaw', 'Kimball', 'Kimble', 'King', 'King and Queen', 'Kings', 'Kiowa', 'Kit Carson', 'Kitsap', 'Kittitas', 'Kittson', 'Klamath', 'Kleberg', 'Klickitat', 'Knox', 'Koochiching', 'Kootenai', 'Kosciusko', 'Kossuth', 'La Crosse', 'La Plata', 'La Salle', 'LaPorte', 'LaSalle', 'Labette', 'Lac qui Parle', 'Lafayette', 'Lafourche', 'Lake', 'Lake of the Woods', 'Lamar', 'Lamoille', 'Lampasas', 'Lancaster', 'Lander', 'Lane', 'Langlade', 'Lapeer', 'Laramie', 'Larimer', 'Las Animas', 'Lauderdale', 'Laurel', 'Laurens', 'Lawrence', 'Le Flore', 'Lea', 'Lebanon', 'Lee', 'Lehigh', 'Lemhi', 'Lenawee', 'Lenoir', 'Leon', 'Lewis', 'Lewis and Clark', 'Lexington', 'Liberty', 'Licking', 'Limestone', 'Lincoln', 'Linn', 'Livingston', 'Llano', 'Logan', 'Lorain', 'Los Alamos', 'Los Angeles', 'Loudoun', 'Louisa', 'Lowndes', 'Lubbock', 'Lucas', 'Luce', 'Luna', 'Luzerne', 'Lycoming', 'Lyon', 'Mackinac', 'Macomb', 'Macon', 'Macon-Bibb County', 'Madera', 'Madison', 'Mahaska', 'Malheur', 'Manassas', 'Manatee', 'Manistee', 'Manitowoc', 'Marathon', 'Marengo', 'Maricopa', 'Maries', 'Marin', 'Marion', 'Marlboro', 'Marquette', 'Marshall', 'Martin', 'Mason', 'Massac', 'Matagorda', 'Maury', 'McCracken', 'McCulloch', 'McCurtain', 'McDonough', 'McDuffie', 'McKean', 'McKenzie', 'McKinley', 'McLean', 'McLennan', 'McLeod', 'McMinn', 'Meade', 'Mecklenburg', 'Mecosta', 'Medina', 'Meeker', 'Mendocino', 'Menominee', 'Merced', 'Mercer', 'Merrimack', 'Mesa', 'Miami', 'Miami-Dade', 'Middlesex', 'Midland', 'Milam', 'Millard', 'Mille Lacs', 'Miller', 'Milwaukee', 'Mineral', 'Minnehaha', 'Mississippi', 'Missoula', 'Mobile', 'Modoc', 'Moffat', 'Mohave', 'Monmouth', 'Mono', 'Monongalia', 'Monroe', 'Montague', 'Monterey', 'Montezuma', 'Montgomery', 'Montrose', 'Moore', 'Morehouse', 'Morgan', 'Morris', 'Morrison', 'Morton', 'Mountrail', 'Mower', 'Multnomah', 'Murray', 'Muscatine', 'Muscogee', 'Muskegon', 'Muskingum', 'Muskogee', 'Nacogdoches', 'Nantucket', 'Napa', 'Nash', 'Nassau', 'Natchitoches', 'Natrona', 'Navajo', 'Navarro', 'Neosho', 'Nevada', 'New Castle', 'New Hanover', 'New Haven', 'New London', 'New York', 'Newaygo', 'Newberry', 'Newport', 'Newport News', 'Newton', 'Nez Perce', 'Niagara', 'Nobles', 'Nolan', 'Norfolk', 'Nueces', 'Nye', "O'Brien", 'Oakland', 'Obion', 'Ocean', 'Ochiltree', 'Oconee', 'Oconto', 'Oglala Lakota', 'Ogle', 'Ohio', 'Okaloosa', 'Okanogan', 'Okeechobee', 'Oklahoma', 'Okmulgee', 'Oktibbeha', 'Olmsted', 'Oneida', 'Onondaga', 'Onslow', 'Orange', 'Orangeburg', 'Orleans', 'Osage', 'Osceola', 'Oswego', 'Otero', 'Otoe', 'Otsego', 'Ottawa', 'Otter Tail', 'Ouachita', 'Outagamie', 'Oxford', 'Page', 'Palm Beach', 'Park', 'Parker', 'Pasco', 'Pasquotank', 'Paulding', 'Payne', 'Pecos', 'Pembina', 'Pennington', 'Penobscot', 'Peoria', 'Perkins', 'Pershing', 'Person', 'Pettis', 'Phelps', 'Philadelphia', 'Phillips', 'Pickens', 'Pierce', 'Pike', 'Pima', 'Pinal', 'Pine', 'Pinellas', 'Pipestone', 'Piscataquis', 'Pitkin', 'Pitt', 'Pittsburg', 'Placer', 'Plaquemines', 'Platte', 'Plymouth', 'Pointe Coupee', 'Polk', 'Pontotoc', 'Pope', 'Portage', 'Porter', 'Pottawatomie', 'Pottawattamie', 'Potter', 'Power', 'Poweshiek', 'Prairie', 'Pratt', 'Presidio', 'Presque Isle', 'Price', "Prince George's", 'Providence', 'Prowers', 'Pueblo', 'Pulaski', 'Quay', "Queen Anne's", 'Queens', 'Racine', 'Raleigh', 'Ramsey', 'Randolph', 'Rankin', 'Rapides', 'Ravalli', 'Red River', 'Red Willow', 'Redwood', 'Reeves', 'Reno', 'Renville', 'Rice', 'Richardson', 'Richland', 'Richmond', 'Riley', 'Rio Arriba', 'Rio Blanco', 'Riverside', 'Roanoke City', 'Roberts', 'Robertson', 'Robeson', 'Rock', 'Rock Island', 'Rockingham', 'Rockwall', 'Rogers', 'Rolette', 'Roosevelt', 'Roscommon', 'Roseau', 'Rosebud', 'Routt', 'Rowan', 'Rusk', 'Russell', 'Rutherford', 'Rutland', 'Sabine', 'Sacramento', 'Saginaw', 'Saguache', 'Saline', 'Salt Lake', 'Sampson', 'San Benito', 'San Bernardino', 'San Diego', 'San Joaquin', 'San Juan', 'San Luis Obispo', 'San Mateo', 'San Miguel', 'San Patricio', 'Sanders', 'Sandoval', 'Sangamon', 'Santa Barbara', 'Santa Clara', 'Santa Cruz', 'Santa Fe', 'Santa Rosa', 'Sarasota', 'Sargent', 'Sarpy', 'Sauk', 'Saunders', 'Sawyer', 'Schenectady', 'Schoolcraft', 'Scotland', 'Scott', 'Scotts Bluff', 'Screven', 'Scurry', 'Sebastian', 'Sedgwick', 'Seminole', 'Sequoyah', 'Sevier', 'Seward', 'Shasta', 'Shawano', 'Shawnee', 'Sheboygan', 'Shelby', 'Sherburne', 'Sheridan', 'Sherman', 'Shiawassee', 'Sierra', 'Silver Bow', 'Sioux', 'Siskiyou', 'Skagit', 'Smith', 'Smyth', 'Snohomish', 'Snyder', 'Socorro', 'Solano', 'Somerset', 'Sonoma', 'Spalding', 'Spartanburg', 'Spokane', 'Spotsylvania', 'St. Charles', 'St. Clair', 'St. Croix', 'St. Francois', 'St. Johns', 'St. Joseph', 'St. Landry', 'St. Lawrence', 'St. Louis', 'St. Louis County', 'St. Lucie', 'St. Mary', "St. Mary's", 'St. Tammany', 'Stafford', 'Stanislaus', 'Stanly', 'Stark', 'Starke', 'Stearns', 'Steele', 'Stephens', 'Stephenson', 'Steuben', 'Stevens', 'Stone', 'Story', 'Strafford', 'Stutsman', 'Sublette', 'Suffolk', 'Sullivan', 'Summit', 'Sumter', 'Surry', 'Sussex', 'Sutton', 'Sweetwater', 'Swift', 'Talbot', 'Tallapoosa', 'Taney', 'Tangipahoa', 'Taos', 'Tarrant', 'Taylor', 'Tazewell', 'Tehama', 'Terrebonne', 'Terrell', 'Teton', 'Texas', 'Thayer', 'Thomas', 'Thurston', 'Tift', 'Tillamook', 'Tillman', 'Tippecanoe', 'Tishomingo', 'Titus', 'Todd', 'Tom Green', 'Tompkins', 'Tooele', 'Toombs', 'Torrance', 'Towner', 'Traverse', 'Travis', 'Trinity', 'Tripp', 'Troup', 'Trumbull', 'Tulare', 'Tulsa', 'Tunica', 'Tuolumne', 'Tuscaloosa', 'Tuscarawas', 'Tuscola', 'Twin Falls', 'Uinta', 'Uintah', 'Umatilla', 'Union', 'Upshur', 'Upson', 'Utah', 'Uvalde', 'Val Verde', 'Valencia', 'Valley', 'Van Buren', 'Vanderburgh', 'Venango', 'Ventura', 'Vermilion', 'Vernon', 'Vigo', 'Vilas', 'Virginia Beach', 'Volusia', 'Wadena', 'Wake', 'Walker', 'Walla Walla', 'Waller', 'Walsh', 'Walton', 'Walworth', 'Wapello', 'Ward', 'Ware', 'Warren', 'Wasatch', 'Waseca', 'Washakie', 'Washington', 'Washita', 'Washoe', 'Washtenaw', 'Watauga', 'Watonwan', 'Waukesha', 'Waupaca', 'Waushara', 'Wayne', 'Webb', 'Weber', 'Webster', 'Weld', 'Wells', 'Westchester', 'Westmoreland', 'Weston', 'Wexford', 'Wharton', 'Whatcom', 'Wheatland', 'White', 'White Pine', 'Whiteside', 'Whitfield', 'Whitman', 'Wichita', 'Wicomico', 'Wilbarger', 'Wilkes', 'Will', 'Williams', 'Williamsburg', 'Williamson', 'Windham', 'Windsor', 'Winkler', 'Winnebago', 'Winneshiek', 'Winona', 'Winston', 'Wise', 'Wood', 'Woodbury', 'Woods', 'Woodward', 'Worcester', 'Wright', 'Wyoming', 'Yakima', 'Yamhill', 'Yankton', 'Yates', 'Yavapai', 'Yellow Medicine', 'Yellowstone', 'Yolo', 'York', 'Young', 'Yuba', 'Yuma'];
function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function (e) {
    var a, b, i, val = this.value;
    /*close any already open lists of autocompleted values*/
    closeAllLists();
    if (!val) { return false; }
    currentFocus = -1;
    /*create a DIV element that will contain the items (values):*/
    a = document.createElement("DIV2");
    a.setAttribute("id", this.id + "autocomplete-list2");
    a.setAttribute("class", "autocomplete-items2");
    /*append the DIV element as a child of the autocomplete container:*/
    this.parentNode.appendChild(a);
    /*for each item in the array...*/
    for (i = 0; i < arr.length; i++) {
      /*check if the item starts with the same letters as the text field value:*/
      if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
        /*create a DIV element for each matching element:*/
        b = document.createElement("DIV");
        /*make the matching letters bold:*/
        b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
        b.innerHTML += arr[i].substr(val.length);
        /*insert a input field that will hold the current array item's value:*/
        b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
        /*execute a function when someone clicks on the item value (DIV element):*/
        b.addEventListener("click", function (e) {
          /*insert the value for the autocomplete text field:*/
          inp.value = this.getElementsByTagName("input")[0].value;
          /*close the list of autocompleted values,
          (or any other open lists of autocompleted values:*/
          closeAllLists();
        });
        a.appendChild(b);
      }
    }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function (e) {
    var x = document.getElementById(this.id + "autocomplete-list2");
    if (x) x = x.getElementsByTagName("div");
    if (e.keyCode == 40) {
      /*If the arrow DOWN key is pressed,
      increase the currentFocus variable:*/
      currentFocus++;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 38) { //up
      /*If the arrow UP key is pressed,
      decrease the currentFocus variable:*/
      currentFocus--;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 13) {
      /*If the ENTER key is pressed, prevent the form from being submitted,*/
      e.preventDefault();
      if (currentFocus > -1) {
        /*and simulate a click on the "active" item:*/
        if (x) x[currentFocus].click();
      }
    }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active2");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active2");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items2");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
    closeAllLists(e.target);
  });
}
autocomplete(document.getElementById('countyinput'), counties);