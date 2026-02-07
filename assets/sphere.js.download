(function ($) {
  "use strict";
  var pxl_widget_sphere_handler = function ($scope, $) {
    const sphereEl = $scope.find(".pxl-sphere.layout-1");
    if (!sphereEl.length) return;
    const canvas = $scope.find("canvas")[0];
    if (!canvas) return;

    const sphereColor = sphereEl.data("color") || "#D7D7D7";

    const size = parseInt(sphereEl.data("size")) || 400;
    const speed = parseFloat(sphereEl.data("speed")) || 0.002;

    canvas.style.width = size + "px";
    canvas.style.height = size + "px";
    canvas.style.display = "block";

    const scene = new THREE.Scene();

    const cssWidth = size;
    const cssHeight = size;
    const aspect = cssWidth / cssHeight;

    const camera = new THREE.PerspectiveCamera(45, aspect, 0.1, 1000);
    camera.position.z = 2.65;
    camera.updateProjectionMatrix();

    const renderer = new THREE.WebGLRenderer({
      canvas,
      alpha: true,
      antialias: true,
    });

    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    renderer.setPixelRatio(dpr);

    renderer.setSize(cssWidth * dpr, cssHeight * dpr, false);

    renderer.domElement.style.width = cssWidth + "px";
    renderer.domElement.style.height = cssHeight + "px";
    renderer.setClearColor(0x000000, 0);
    
    const textureLoader = new THREE.TextureLoader();
    const imgUrl = sphereEl.data("img");
    if (!imgUrl) return;
    const globeTexture = textureLoader.load(imgUrl);

    globeTexture.wrapS = THREE.RepeatWrapping;
    globeTexture.wrapT = THREE.RepeatWrapping;
    globeTexture.repeat.set(4, 1);

    const geometry = new THREE.SphereGeometry(1, 64, 64);
    const material = new THREE.MeshPhongMaterial({
      map: globeTexture,
      color: new THREE.Color(sphereColor),
      emissive: new THREE.Color(sphereColor),
      emissiveIntensity: 0.6, 
      transparent: true,
      // side: THREE.DoubleSide,
      shininess: 10,
    });
    const globe = new THREE.Mesh(geometry, material);
    scene.add(globe);

    const ambient = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambient);
    const directional = new THREE.DirectionalLight(0xffffff, 1);
    directional.position.set(5, 3, 5);
    scene.add(directional);

    globe.rotation.x = Math.PI / 8;

    const rotationType = sphereEl.data("rotation") || "y_axis";
    function animate() {
        requestAnimationFrame(animate);
        switch (rotationType) {
            case "y_axis":
            globe.rotation.y += speed;
            break;
            case "x_axis":
            globe.rotation.x += speed;
            break;
            case "both_axis":
            globe.rotation.y += speed;
            globe.rotation.x += speed / 2;
            break;
        }
        renderer.render(scene, camera);
    }
    animate();

    function handleResize() {
      const newCssW = canvas.clientWidth || cssWidth;
      const newCssH = canvas.clientHeight || cssHeight;
      const newAspect = newCssW / newCssH;

      camera.aspect = newAspect;
      camera.updateProjectionMatrix();

      const newDpr = Math.min(window.devicePixelRatio || 1, 2);
      renderer.setPixelRatio(newDpr);
      renderer.setSize(newCssW * newDpr, newCssH * newDpr, false);

      renderer.domElement.style.width = newCssW + "px";
      renderer.domElement.style.height = newCssH + "px";
    }

    window.addEventListener("resize", handleResize);

    (function checkParentOverflow() {
      let p = canvas.parentElement;
      while (p) {
        const style = window.getComputedStyle(p);
        if (style.overflow === "hidden" || style.overflowX === "hidden" || style.overflowY === "hidden") {
          break;
        }
        p = p.parentElement;
      }
    })();
  };

  var pxl_widget_sphere_handler2 = function ($scope, $) {
        const canvas = $scope.find(".pxl-sphere.layout-2 canvas");
        if (!canvas.length) return;

        const sphereEl = $scope.find(".pxl-sphere.layout-2");
        if (!sphereEl.length) return;
        const size = parseInt(sphereEl.data("size")) || 400;
        const radius = parseInt(sphereEl.data("radius")) || size * 0.3;Math.PI
        const sphereColor = sphereEl.data("color") || "#2458F6";
        const rotationType = sphereEl.data("rotation") || "y_axis";
        const rotationSpeed = parseFloat(sphereEl.data("speed")) || 0.005;
        const customXSpeed = parseFloat(sphereEl.data("xspeed")) || 0.003;
        const customYSpeed = parseFloat(sphereEl.data("yspeed")) || 0.005;
        const tiltAngle =
            ((parseFloat(sphereEl.data("tilt")) || -30) * Math.PI) / 180;

        const ctx = canvas[0].getContext("2d");

        canvas[0].width = size;
        canvas[0].height = size;

        let angleX = tiltAngle;
        let angleY = 0;

        function rotate(point, angleX, angleY) {
            let cosX = Math.cos(angleX),
                sinX = Math.sin(angleX);
            let cosY = Math.cos(angleY),
                sinY = Math.sin(angleY);

            let y = point.y * cosX - point.z * sinX;
            let z = point.y * sinX + point.z * cosX;
            let x = point.x * cosY - z * sinY;
            z = point.x * sinY + z * cosY;
            return { x, y, z };
        }

        function drawSphere() {
            ctx.clearRect(0, 0, canvas[0].width, canvas[0].height);
            ctx.strokeStyle = sphereColor;
            ctx.lineWidth = 1;
            const cx = canvas[0].width / 2;
            const cy = canvas[0].height / 2;

            for (
                let lat = -Math.PI / 2;
                lat <= Math.PI / 2;
                lat += Math.PI / 6
            ) {
                let circlePoints = [];
                for (let lon = 0; lon < 2 * Math.PI; lon += Math.PI / 20) {
                    let x = Math.cos(lat) * Math.cos(lon);
                    let y = Math.sin(lat);
                    let z = Math.cos(lat) * Math.sin(lon);
                    let rotatedPoint = rotate({ x, y, z }, angleX, angleY);
                    circlePoints.push(rotatedPoint);
                }
                ctx.beginPath();
                circlePoints.forEach((p, i) => {
                    if (i === 0) {
                        ctx.moveTo(cx + p.x * radius, cy + p.y * radius);
                    } else {
                        ctx.lineTo(cx + p.x * radius, cy + p.y * radius);
                    }
                });
                ctx.closePath();
                ctx.stroke();
            }

            for (let lon = 0; lon < 2 * Math.PI; lon += Math.PI / 6) {
                let circlePoints = [];
                for (
                    let lat = -Math.PI / 2;
                    lat <= Math.PI / 2;
                    lat += Math.PI / 20
                ) {
                    let x = Math.cos(lat) * Math.cos(lon);
                    let y = Math.sin(lat);
                    let z = Math.cos(lat) * Math.sin(lon);
                    let rotatedPoint = rotate({ x, y, z }, angleX, angleY);
                    circlePoints.push(rotatedPoint);
                }
                ctx.beginPath();
                circlePoints.forEach((p, i) => {
                    if (i === 0) {
                        ctx.moveTo(cx + p.x * radius, cy + p.y * radius);
                    } else {
                        ctx.lineTo(cx + p.x * radius, cy + p.y * radius);
                    }
                });
                ctx.stroke();
            }
        }

        function updateRotation() {
            switch (rotationType) {
                case "y_axis":
                    angleY += rotationSpeed;
                    break;
                case "x_axis":
                    angleX += rotationSpeed;
                    break;
                case "both_axis":
                    angleX += rotationSpeed;
                    angleY += rotationSpeed;
                    break;
                case "custom":
                    angleX += customXSpeed;
                    angleY += customYSpeed;
                    break;
            }
        }

        function animate() {
            updateRotation();
            drawSphere();
            requestAnimationFrame(animate);
        }

        animate();
  };

  $(window).on("elementor/frontend/init", function () {
    if (typeof elementorFrontend === "undefined" || !elementorFrontend.hooks) return;
    elementorFrontend.hooks.addAction("frontend/element_ready/pxl_sphere.default", pxl_widget_sphere_handler);
    elementorFrontend.hooks.addAction("frontend/element_ready/pxl_sphere.default", pxl_widget_sphere_handler2);
  });
})(jQuery);
