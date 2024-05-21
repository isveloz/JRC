from django.core.management.base import BaseCommand
from myapp.models import Marca, TipoHerramienta, Producto, Genero, TipoEmpleado, Empleado

class Command(BaseCommand):
    help = 'Initialize the database with sample products and other models'

    def handle(self, *args, **kwargs):
        # Crear marcas
        marcas = [
            "Stanley", "Indurarc", "Volcán", "Acma", "Inchalam", "Inppa"
        ]
        for marca_desc in marcas:
            Marca.objects.create(descripcion=marca_desc)

        # Crear tipos de herramientas
        tipos_herramienta = [
            "Esmeril", "Soldadora", "Sierra Circular", "Aislante", "Cinta", "Cadena", "Volcanita", "Malla", "Teja"
        ]
        for tipo_desc in tipos_herramienta:
            TipoHerramienta.objects.create(description=tipo_desc)

        # Crear productos
        productos = [
            {
                'nombre': "STANLEY ESMERIL ANGULAR 4 1/2\" 750 W SG7115B2C DW + 10 DISCOS DE REGALO STANLEY",
                'tipo': TipoHerramienta.objects.get(description="Esmeril"),
                'descripcion': "Esmeril con óptima salida de flujo de aire que evita el sobrecalentamiento del motor. Incluye 10 discos de corte ultrafino para metal inoxidable, lo que ofrece cortes más rápidos y precisos.",
                'marca': Marca.objects.get(descripcion="Stanley"),
                'imagen': 'core/img/herramientas/211346-800-auto.webp',
                'precio': 24990,
            },
            {
                'nombre': "SOLDADORA INVERSORA INDURARC 120",
                'tipo': TipoHerramienta.objects.get(description="Soldadora"),
                'descripcion': "La máquina de soldar inversora INDURARC 120 utiliza IGBTs como componente principal de su sistema electrónico, los que han sido especialmente desarrollados para controlar y mantener estable el arco eléctrico al momento de soldar.",
                'marca': Marca.objects.get(descripcion="Indurarc"),
                'imagen': 'core/img/herramientas/soldadora.webp',
                'precio': 79990,
            },
            {
                'nombre': "STANLEY SIERRA CIRCULAR 7 1/4\" 1600 W",
                'tipo': TipoHerramienta.objects.get(description="Sierra Circular"),
                'descripcion': "Como parte de la gama de herramientas eléctricas con cable STANLEY FATMAX®, esta sierra circular tiene un potente motor de 1.600 W y ofrece un verdadero rendimiento profesional. Una sierra circular es imprescindible en todos los sentidos.",
                'marca': Marca.objects.get(descripcion="Stanley"),
                'imagen': 'core/img/herramientas/196408-800---auto.webp',
                'precio': 30000,
            },
            {
                'nombre': "VOLCÁN ROLLO LANA DE VIDRIO LIBRE R94 40 MM 1,2 X 24 MT 28,8 M2",
                'tipo': TipoHerramienta.objects.get(description="Aislante"),
                'descripcion': "Es una de las opciones más seguras y eficientes para el aislamiento térmico y acústico en el mercado actual. Este material aislante es altamente resistente al fuego y a altas temperaturas, lo que lo hace ideal para su uso en aplicaciones industriales y comerciales donde se requiere un alto nivel de seguridad y protección.",
                'marca': Marca.objects.get(descripcion="Volcán"),
                'imagen': 'core/img/construccion/194827-300-300.webp',
                'precio': 41570,
            },
            {
                'nombre': "VOLCÁN HUINCHA JUNTAPRO FV 50 MM 45 MT",
                'tipo': TipoHerramienta.objects.get(description="Cinta"),
                'descripcion': "La Cinta de Fibra de Vidrio JuntaPro Volcán® consiste en una malla de fibra de vidrio autoadhesiva, que posee una gran resistencia mecánica, y que se usa en el tratamiento de juntas invisibles de tabiques.",
                'marca': Marca.objects.get(descripcion="Volcán"),
                'imagen': 'core/img/construccion/207490-300-300.webp',
                'precio': 3590,
            },
            {
                'nombre': "ACMA CADENA 15 X 30 CM 4,5 MT FE 9,2 MM",
                'tipo': TipoHerramienta.objects.get(description="Cadena"),
                'descripcion': "Esta diseñada para soportar elevadas cargas, indispensable su uso en trabajos industriales y de construcción para armadura y refuerzo de estructura de marco, coronamiento de albañilerías, coronamiento de muros cortafuego, vanos de puertas y ventanas.",
                'marca': Marca.objects.get(descripcion="Acma"),
                'imagen': 'core/img/construccion/193849-300-300.webp',
                'precio': 23990,
            },
            {
                'nombre': "VOLCÁN VOLCANITA ESTÁNDAR BORDE BISELADO 8 MM 1,2 X 2,4 MT",
                'tipo': TipoHerramienta.objects.get(description="Volcanita"),
                'descripcion': "Las planchas yeso cartón estándar son usadas en tabiques divisorios, cielos, revestimientos de muro y soluciones constructivas tales como tabique estructural y tabique volcometal.",
                'marca': Marca.objects.get(descripcion="Volcán"),
                'imagen': 'core/img/construccion/194832-300-300.webp',
                'precio': 6690,
            },
            {
                'nombre': "INCHALAM MALLA HARNERO N°8 0,6 X 1,5 MT",
                'tipo': TipoHerramienta.objects.get(description="Malla"),
                'descripcion': "Malla tejida de alambre, fabricada especialmente para realizar tus trabajos de tamizado o limpieza de semillas. Su uso varía entre tamizado de tierra para jardín, tamizado de arena para mezcla y estuco, limpieza de semillas.",
                'marca': Marca.objects.get(descripcion="Inchalam"),
                'imagen': 'core/img/construccion/194011-300-300.webp',
                'precio': 14990,
            },
            {
                'nombre': "INPPA TEJA ASTURIAS LÍNEA CONTINUA 0,4 X 1010 X 3660 MM NEGRA",
                'tipo': TipoHerramienta.objects.get(description="Teja"),
                'descripcion': "Ideal para ampliaciones, cobertizos, entre otros, de gran durabilidad. Ofrece gran maniobrabilidad por su bajo peso al momento de instalar y proporciona alta resistencia al impacto, como así también cuando se ejecutan cargas puntuales dada su conformación en acero.",
                'marca': Marca.objects.get(descripcion="Inppa"),
                'imagen': 'core/img/construccion/206793-300-300.webp',
                'precio': 30390,
            }
        ]

        for producto in productos:
            Producto.objects.create(**producto)

        self.stdout.write(self.style.SUCCESS('Successfully initialized the database with sample products'))
