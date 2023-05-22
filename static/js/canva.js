const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

fetch('/get_motion_vision_data/')  // URL a tu vista Django que devuelve los datos necesarios
  .then(response => response.json())
  .then(data => {
    const optotypes = JSON.parse(data.optotypes_json);
    const optotypeOrder = data.optotype_order;
    const rotationSpeed = data.rotation_speed;
    const correctDirection = data.correct_direction;

    let currentOptotypeIndex = 0;
    let rotationAngle = 0;

    function draw() {
      // Código para dibujar y animar los optotipos en el canvas aquí
    }

    // Resto del código para el dibujo y animación de los optotipos

    draw();
  })
  .catch(error => console.error(error));
