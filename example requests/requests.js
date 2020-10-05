// GET /{module}/{api-format}

var settings = {
  "url": "https://munch.emuseum.com/objects/json?key={key}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /{module}/{id}/{api-format}

var settings = {
  "url": "https://munch.emuseum.com/objects/4714/json?key={key}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /search/{keyword}/{module}/{api-format}

var settings = {
  "url": "https://munch.emuseum.com/search/skrik/objects/json?key={key}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /advancedsearch/{module}/{field}:{field-value}/{api-format}

var settings = {
  "url": "https://munch.emuseum.com/advancedsearch/objects/title:skrik/json?key={key}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /{module}/{api-format}?filter

var settings = {
  "url": "https://munch.emuseum.com/objects/json?filter=thesfilter:1545220&key={key}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /{search}/{keyword}/{module}/{api-format}?filter

var settings = {
  "url": "https://munch.emuseum.com/search/skrik/objects/json?filter=department:Munch-samlingen&key={key}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /{module}/{api-format}?page

var settings = {
  "url": "http://munch.emuseum.com/objects/json?page=2&key={key}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /{module}/{api-format}?sort

var settings = {
  "url": "https://munch.emuseum.com/objects/json?sort=displayDate-asc&key={key}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /search/{keyword}/{module}/{api-format}?sort

var settings = {
  "url": "https://munch.emuseum.com/search/skrik/objects/json?sort=invno-asc&key={key}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


// GET /advancedsearch/{module}/{field}:{field-value}/{api-format}?sort

var settings = {
  "url": "https://munch.emuseum.com/advancedsearch/objects/title:skrik/json?sort=displayDate-asc&key={key}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
