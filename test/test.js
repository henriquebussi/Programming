fetch("./chest.json")
  .then((response) => response.json())
  .then((json) => console.log(json))
  .catch((error) => console.error('Error fetching JSON:', error));
