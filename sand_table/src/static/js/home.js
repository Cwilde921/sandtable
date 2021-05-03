document.getElementById("btn1").onclick = () => {
    fetch(location.href+"/api",{
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'hello': "world"})
    })//.then((res) => res.json())
      .then((res) => console.log(res))
}