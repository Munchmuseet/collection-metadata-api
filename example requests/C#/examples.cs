// GET /{module}/{api-format}

var client = new RestClient("https://munch.emuseum.com/objects/json?key={key}");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);


// GET /{module}/{id}/{api-format}

var client = new RestClient("https://munch.emuseum.com/objects/4714/json?key={key}");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);


// GET /search/{keyword}/{module}/{api-format}

var client = new RestClient("https://munch.emuseum.com/search/skrik/objects/json?key={key}");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);


// GET /advancedsearch/{module}/{field}:{field-value}/{api-format}

var client = new RestClient("https://munch.emuseum.com/advancedsearch/objects/title:skrik/json?key={key}");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);


// GET /{module}/{api-format}?filter

var client = new RestClient("https://munch.emuseum.com/objects/json?filter=thesfilter:1545220&key={key}");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);


// GET /{search}/{keyword}/{module}/{api-format}?filter

var client = new RestClient("https://munch.emuseum.com/search/skrik/objects/json?filter=department:Munch-samlingen&key={key}");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);


// GET /{module}/{api-format}?page

var client = new RestClient("http://munch.emuseum.com/objects/json?page=2&key={key}");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);


// GET /{module}/{api-format}?sort

var client = new RestClient("https://munch.emuseum.com/objects/json?sort=displayDate-asc&key={key}");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);

// GET /search/{keyword}/{module}/{api-format}?sort

var client = new RestClient("https://munch.emuseum.com/search/skrik/objects/json?sort=invno-asc&key={key}");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);


// GET /advancedsearch/{module}/{field}:{field-value}/{api-format}?sort

var client = new RestClient("https://munch.emuseum.com/advancedsearch/objects/title:skrik/json?sort=displayDate-asc&key={key}");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
