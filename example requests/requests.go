# GET /{module}/{api-format}

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/objects/json?key=%7Bkey%7D"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /{module}/{id}/{api-format}

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/objects/4714/json?key=%7Bkey%7D"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /search/{keyword}/{module}/{api-format}

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/search/skrik/objects/json?key=%7Bkey%7D"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /advancedsearch/{module}/{field}:{field-value}/{api-format}

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/advancedsearch/objects/title:skrik/json?key=%7Bkey%7D"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /{module}/{api-format}?filter

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/objects/json?filter=thesfilter:1545220&key=%7Bkey%7D"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /{search}/{keyword}/{module}/{api-format}?filter

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/search/skrik/objects/json?filter=department:Munch-samlingen&key=%7Bkey%7D"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /{module}/{api-format}?page

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "http://munch.emuseum.com/objects/json?page=2&key=%7Bkey%7D"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /{module}/{api-format}?sort

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/objects/json?sort=displayDate-asc&key=%7Bkey%7D"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /search/{keyword}/{module}/{api-format}?sort

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/search/skrik/objects/json?sort=invno-asc&key=%7Bkey%7D"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}


# GET /advancedsearch/{module}/{field}:{field-value}/{api-format}?sort

package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://munch.emuseum.com/advancedsearch/objects/title:skrik/json?sort=displayDate-asc&key=%7Bkey%7D"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}
