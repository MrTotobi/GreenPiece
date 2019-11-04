jQuery(function($) {
    var locations = {
        'Región Metropolitana de Santiago': [
            "Cerrillos",
            "Cerro Navia",
            "Conchalí",
            "El Bosque",
            "Estación Central",
            "Huechuraba",
            "Independencia",
            "La Cisterna",
            "La Florida",
            "La Granja",
            "La Pintana",
            "La Reina",
            "Las Condes",
            "Lo Barnechea",
            "Lo Espejo",
            "Lo Prado",
            "Macul",
            "Maipú",
            "Ñuñoa",
            "Pedro Aguirre Cerda",
            "Peñalolén",
            "Providencia",
            "Pudahuel",
            "Quilicura",
            "Quinta Normal",
            "Recoleta",
            "Renca",
            "Santiago",
            "San Joaquín",
            "San Miguel",
            "San Ramón",
            "Vitacura",
            "Puente Alto",
            "Pirque",
            "San José de Maipo",
            "Colina",
            "Lampa",
            "Tiltil",
            "San Bernardo",
            "Buin",
            "Calera de Tango",
            "Paine",
            "Melipilla",
            "Alhué",
            "Curacaví",
            "María Pinto",
            "San Pedro",
            "Talagante",
            "El Monte",
            "Isla de Maipo",
            "Padre Hurtado",
            "Peñaflor"
        ],
        'Tarapacá': [
            "Iquique",
            "Alto Hospicio",
            "Pozo Almonte",
            "Camiña",
            "Colchane",
            "Huara",
            "Pica"
        ],
        'Antofagasta': [
            "Antofagasta",
            "Mejillones",
            "Sierra Gorda",
            "Taltal",
            "Calama",
            "Ollagüe",
            "San Pedro de Atacama",
            "Tocopilla",
            "María Elena"
        ],
        'Atacama': [
            "Copiapó",
            "Caldera",
            "Tierra Amarilla",
            "Chañaral",
            "Diego de Almagro",
            "Vallenar",
            "Alto del Carmen",
            "Freirina",
            "Huasco"
        ],
        'Coquimbo': [
            "La Serena",
            "Coquimbo",
            "Andacollo",
            "La Higuera",
            "Paiguano",
            "Vicuña",
            "Illapel",
            "Canela",
            "Los Vilos",
            "Salamanca",
            "Ovalle",
            "Combarbalá",
            "Monte Patria",
            "Punitaqui",
            "Río Hurtado"
        ],
        'Valparaíso': [
            "Valparaíso",
            "Casablanca",
            "Concón",
            "Juan Fernández",
            "Puchuncaví",
            "Quintero",
            "Viña del Mar",
            "Isla de Pascua",
            "Los Andes",
            "Calle Larga",
            "Rinconada",
            "San Esteban",
            "La Ligua",
            "Cabildo",
            "Papudo",
            "Petorca",
            "Zapallar",
            "Quillota",
            "Calera",
            "Hijuelas",
            "La Cruz",
            "Nogales",
            "San Antonio",
            "Algarrobo",
            "Cartagena",
            "El Quisco",
            "El Tabo",
            "Santo Domingo",
            "San Felipe",
            "Catemu",
            "Llaillay",
            "Panquehue",
            "Putaendo",
            "Santa María",
            "Quilpué",
            "Limache",
            "Olmué",
            "Villa Alemana"
        ],
        'Región del Libertador Gral. Bernardo O’Higgins': [
            "Rancagua",
            "Codegua",
            "Coinco",
            "Coltauco",
            "Doñihue",
            "Graneros",
            "Las Cabras",
            "Machalí",
            "Malloa",
            "San Francisco de Mostazal",
            "Olivar",
            "Peumo",
            "Pichidegua",
            "Quinta de Tilcoco",
            "Rengo",
            "Requínoa",
            "San Vicente de Tagua Tagua",
            "Pichilemu",
            "La Estrella",
            "Litueche",
            "Marchihue",
            "Navidad",
            "Paredones",
            "San Fernando",
            "Chépica",
            "Chimbarongo",
            "Lolol",
            "Nancagua",
            "Palmilla",
            "Peralillo",
            "Placilla",
            "Pumanque",
            "Santa Cruz"
        ],
        'Región del Maule': [
            "Talca",
            "Constitución",
            "Curepto",
            "Empedrado",
            "Maule",
            "Pelarco",
            "Pencahue",
            "Río Claro",
            "San Clemente",
            "San Rafael",
            "Cauquenes",
            "Chanco",
            "Pelluhue",
            "Curicó",
            "Hualañé",
            "Licantén",
            "Molina",
            "Rauco",
            "Romeral",
            "Sagrada Familia",
            "Teno",
            "Vichuquén",
            "Linares",
            "Colbún",
            "Longaví",
            "Parral",
            "Retiro",
            "San Javier de Loncomilla",
            "Villa Alegre",
            "Yerbas Buenas"
        ],
        'Región del Biobío': [
            "Concepción",
            "Coronel",
            "Chiguayante",
            "Florida",
            "Hualqui",
            "Lota",
            "Penco",
            "San Pedro de la Paz",
            "Santa Juana",
            "Talcahuano",
            "Tomé",
            "Hualpén",
            "Lebu",
            "Arauco",
            "Cañete",
            "Contulmo",
            "Curanilahue",
            "Los Álamos",
            "Tirúa",
            "Los Ángeles",
            "Antuco",
            "Cabrero",
            "Laja",
            "Mulchén",
            "Nacimiento",
            "Negrete",
            "Quilaco",
            "Quilleco",
            "San Rosendo",
            "Santa Bárbara",
            "Tucapel",
            "Yumbel",
            "Alto Biobío"
        ],
        'Región de la Araucanía': [
            "Temuco",
            "Carahue",
            "Cunco",
            "Curarrehue",
            "Freire",
            "Galvarino",
            "Gorbea",
            "Lautaro",
            "Loncoche",
            "Melipeuco",
            "Nueva Imperial",
            "Padre las Casas",
            "Perquenco",
            "Pitrufquén",
            "Pucón",
            "Saavedra",
            "Teodoro Schmidt",
            "Toltén",
            "Vilcún",
            "Villarrica",
            "Cholchol",
            "Angol",
            "Collipulli",
            "Curacautín",
            "Ercilla",
            "Lonquimay",
            "Los Sauces",
            "Lumaco",
            "Purén",
            "Renaico",
            "Traiguén",
            "Victoria"
        ],
        'Región de Los Ríos': [
            "Valdivia",
            "Corral",
            "Lanco",
            "Los Lagos",
            "Máfil",
            "Mariquina",
            "Paillaco",
            "Panguipulli",
            "La Unión",
            "Futrono",
            "Lago Ranco",
            "Río Bueno"
        ],
        'Región de Los Lagos': [
            "Puerto Montt",
            "Calbuco",
            "Cochamó",
            "Fresia",
            "Frutillar",
            "Los Muermos",
            "Llanquihue",
            "Maullín",
            "Puerto Varas",
            "Castro",
            "Ancud",
            "Chonchi",
            "Curaco de Vélez",
            "Dalcahue",
            "Puqueldón",
            "Queilén",
            "Quellón",
            "Quemchi",
            "Quinchao",
            "Osorno",
            "Puerto Octay",
            "Purranque",
            "Puyehue",
            "Río Negro",
            "San Juan de la Costa",
            "San Pablo",
            "Chaitén",
            "Futaleufú",
            "Hualaihué",
            "Palena"
        ],
        'Región Aysén del Gral. Carlos Ibáñez del Campo': [
            "Coihaique",
            "Lago Verde",
            "Aisén",
            "Cisnes",
            "Guaitecas",
            "Cochrane",
            "O’Higgins",
            "Tortel",
            "Chile Chico",
            "Río Ibáñez"
        ],
        'Región de Magallanes y de la Antártica Chilena': [
            "Punta Arenas",
            "Laguna Blanca",
            "Río Verde",
            "San Gregorio",
            "Cabo de Hornos (Ex Navarino)",
            "Antártica",
            "Porvenir",
            "Primavera",
            "Timaukel",
            "Natales",
            "Torres del Paine"
        ],
        'Arica y Parinacota': [
            "Arica",
            "Camarones",
            "Putre",
            "General Lagos"
        ],
        'Región de Ñuble': [
            "Cobquecura",
            "Coelemu",
            "Ninhue",
            "Portezuelo",
            "Quirihue",
            "Ránquil",
            "Treguaco",
            "Bulnes",
            "Chillán Viejo",
            "Chillán",
            "El Carmen",
            "Pemuco",
            "Pinto",
            "Quillón",
            "San Ignacio",
            "Yungay",
            "Coihueco",
            "Ñiquén",
            "San Carlos",
            "San Fabián",
            "San Nicolás"
        ],
    }

    var $locations = $('#location');
    $('#country').change(function() {
        var country = $(this).val(),
            lcns = locations[country] || [];

        var html = $.map(lcns, function(lcn) {
            return '<option value="' + lcn + '">' + lcn + '</option>'
        }).join('');
        $locations.html(html)
    });
});

function setInputFilter(textbox, inputFilter) {
    ["input", "keydown", "keyup", "mousedown", "mouseup", "select", "contextmenu", "drop"].forEach(function(event) {
        textbox.addEventListener(event, function() {
            if (inputFilter(this.value)) {
                this.oldValue = this.value;
                this.oldSelectionStart = this.selectionStart;
                this.oldSelectionEnd = this.selectionEnd;
            } else if (this.hasOwnProperty("oldValue")) {
                this.value = this.oldValue;
                this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
            }
        });
    });
}

setInputFilter(document.getElementById("txtNombre"), function(value) {
    return /^[' '\a-z\u00c0-\u024f]*$/i.test(value);
});

function checkRut(rut) {


    var valor = rut.value.replace('.', '');

    valor = valor.replace('-', '');

    cuerpo = valor.slice(0, -1);
    dv = valor.slice(-1).toUpperCase();

    rut.value = cuerpo + '-' + dv

    if (cuerpo.length < 7) { rut.setCustomValidity("RUT Incompleto"); return false; }

    suma = 0;
    multiplo = 2;

    for (i = 1; i <= cuerpo.length; i++) {

        index = multiplo * valor.charAt(cuerpo.length - i);

        suma = suma + index;

        if (multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }

    }

    dvEsperado = 11 - (suma % 11);

    dv = (dv == 'K') ? 10 : dv;
    dv = (dv == 0) ? 11 : dv;

    if (dvEsperado != dv) { rut.setCustomValidity("RUT Inválido"); return false; }

    rut.setCustomValidity('');
}

function myFunction() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}