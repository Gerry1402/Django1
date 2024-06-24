# Generated by Django 5.0.6 on 2024-06-24 01:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0031_alter_particular_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='particular',
            name='password1',
            field=models.CharField(default='', max_length=31, verbose_name='Crear contraseña'),
        ),
        migrations.AddField(
            model_name='particular',
            name='password2',
            field=models.CharField(default='', max_length=31, verbose_name='Repetir contraseña'),
        ),
        migrations.AlterField(
            model_name='particular',
            name='nacimiento',
            field=models.DateField(default=datetime.datetime(2006, 6, 24, 1, 35, 42, 893497, tzinfo=datetime.timezone.utc), verbose_name='Nacimiento'),
        ),
        migrations.AlterField(
            model_name='particular',
            name='pais_residencia',
            field=models.CharField(choices=[('AF', 'Afganistán'), ('AL', 'Albania'), ('DE', 'Alemania'), ('DZ', 'Algeria'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguila'), ('AG', 'Antigua y Barbuda'), ('AQ', 'Antártida'), ('SA', 'Arabia Saudí'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaiyán'), ('BS', 'Bahamas'), ('BD', 'Bangladés'), ('BB', 'Barbados'), ('BH', 'Baréin'), ('BZ', 'Belice'), ('BJ', 'Benín'), ('BY', 'Bielorrusia'), ('MM', 'Birmania'), ('BO', 'Bolivia, Estado plurinacional de'), ('BA', 'Bosnia y Herzegovina'), ('BW', 'Botsuana'), ('BR', 'Brasil'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burquina Faso'), ('BI', 'Burundi'), ('BT', 'Bután'), ('BE', 'Bélgica'), ('CV', 'Cabo Verde'), ('KH', 'Camboya'), ('CM', 'Camerún'), ('CA', 'Canadá'), ('QA', 'Catar'), ('TD', 'Chad'), ('CZ', 'Chequia'), ('CL', 'Chile'), ('CN', 'China'), ('CY', 'Chipre'), ('CO', 'Colombia'), ('KM', 'Comores, Islas'), ('CG', 'Congo'), ('CD', 'Congo, República Democrática del'), ('KP', 'Corea, República Democrática Popular de'), ('KR', 'Corea, República de'), ('CR', 'Costa Rica'), ('CI', 'Costa de Marfíl'), ('HR', 'Croacia'), ('CU', 'Cuba'), ('CW', 'Curazao'), ('DK', 'Dinamarca'), ('DM', 'Dominica'), ('EC', 'Ecuador'), ('EG', 'Egipto'), ('SV', 'El Salvador'), ('AE', 'Emiratos Árabes Unidos'), ('ER', 'Eritrea'), ('SK', 'Eslovaquia'), ('SI', 'Eslovenia'), ('ES', 'España'), ('US', 'Estados Unidos'), ('EE', 'Estonia'), ('SZ', 'Esuatini'), ('ET', 'Etiopía'), ('RU', 'Federación Rusa'), ('PH', 'Filipinas'), ('FI', 'Finlandia'), ('FJ', 'Fiyi'), ('FR', 'Francia'), ('GA', 'Gabón'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GD', 'Granada'), ('GR', 'Grecia'), ('GL', 'Groenlandia'), ('GP', 'Guadalupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GF', 'Guayana Francesa'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GQ', 'Guinea Ecuatorial'), ('GW', 'Guinea-Bisáu'), ('GY', 'Guyana'), ('HT', 'Haití'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungría'), ('IN', 'India'), ('ID', 'Indonesia'), ('IQ', 'Irak'), ('IE', 'Irlanda'), ('IR', 'Irán, República islámica de'), ('BV', 'Isla Bouvet'), ('NF', 'Isla Norfolk'), ('IM', 'Isla de Man'), ('CX', 'Isla de Navidad'), ('SX', 'Isla de San Martín (zona holandsea)'), ('IS', 'Islandia'), ('BQ', 'Islas BES (Caribe Neerlandés)'), ('BM', 'Islas Bermudas'), ('KY', 'Islas Caimán'), ('CC', 'Islas Cocos (Keeling)'), ('CK', 'Islas Cook'), ('FK', 'Islas Falkland (Malvinas)'), ('FO', 'Islas Feroe'), ('GS', 'Islas Georgias del Sur y Sándwich del Sur'), ('HM', 'Islas Heard y McDonald'), ('MV', 'Islas Maldivas'), ('MP', 'Islas Marianas del Norte'), ('MH', 'Islas Marshall'), ('SB', 'Islas Salomón'), ('TC', 'Islas Turcas y Caicos'), ('UM', 'Islas Ultramarinas Menores de Estados Unidos'), ('VG', 'Islas Vírgenes, Británicas'), ('VI', 'Islas Vírgenes, de EEUU'), ('AX', 'Islas Äland'), ('IL', 'Israel'), ('IT', 'Italia'), ('JM', 'Jamaica'), ('JP', 'Japón'), ('JE', 'Jersey'), ('JO', 'Jordania'), ('KZ', 'Kazajistán'), ('KE', 'Kenia'), ('KG', 'Kirguistán'), ('KI', 'Kiribati'), ('KW', 'Kuwait'), ('LS', 'Lesoto'), ('LV', 'Letonia'), ('LR', 'Liberia'), ('LY', 'Libia'), ('LI', 'Liechtenstein'), ('LT', 'Lituania'), ('LU', 'Luxemburgo'), ('LB', 'Líbano'), ('MO', 'Macao'), ('MK', 'Macedonia del Norte'), ('MG', 'Madagascar'), ('MY', 'Malasia'), ('MW', 'Malaui'), ('MT', 'Malta'), ('ML', 'Malí'), ('MA', 'Marruecos'), ('MQ', 'Martinica'), ('MU', 'Mauricio'), ('MR', 'Mauritania'), ('YT', 'Mayotte'), ('FM', 'Micronesia, Estados Federados de'), ('MD', 'Moldavia, República de'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MZ', 'Mozambique'), ('MX', 'México'), ('MC', 'Mónaco'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NO', 'Noruega'), ('NC', 'Nueva Caledonia'), ('NZ', 'Nueva Zelanda'), ('OM', 'Omán'), ('PK', 'Pakistán'), ('PW', 'Palaos'), ('PS', 'Palestina, Estado de'), ('PA', 'Panamá'), ('PG', 'Papúa Nueva Guinea'), ('PY', 'Paraguay'), ('NL', 'Países Bajos'), ('PE', 'Perú'), ('PN', 'Pitcairn'), ('PF', 'Polinesia Francesa'), ('PL', 'Polonia'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('GB', 'Reino Unido'), ('CF', 'República Centroafricana'), ('LA', 'República Democrática Popular de Lao'), ('DO', 'República Dominicana'), ('SY', 'República árabe de Siria'), ('RE', 'Reunión'), ('RW', 'Ruanda'), ('RO', 'Rumanía'), ('EH', 'Sahara Occidental'), ('WS', 'Samoa'), ('AS', 'Samoa Estadounidense'), ('BL', 'San Bartolomé'), ('KN', 'San Cristóbal y Nieves'), ('SM', 'San Marino'), ('MF', 'San Martín (zona francesa)'), ('PM', 'San Pedro y Miquelon'), ('VC', 'San Vicente y las Granadinas'), ('SH', 'Santa Elena, Ascensión y Tristán de Acuña'), ('LC', 'Santa Lucía'), ('VA', 'Santa Sede (Ciudad Estado del Vaticano)'), ('ST', 'Santo Tomé y Príncipe'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leona'), ('SG', 'Singapur'), ('SO', 'Somalia'), ('LK', 'Sri Lanka'), ('ZA', 'Sudáfrica'), ('SD', 'Sudán'), ('SS', 'Sudán del Sur'), ('SE', 'Suecia'), ('CH', 'Suiza'), ('SR', 'Surinám'), ('SJ', 'Svalbard y Jan Mayen'), ('TH', 'Tailandia'), ('TW', 'Taiwán, Provincia de China'), ('TZ', 'Tanzania, República unida de'), ('TJ', 'Tayikistán'), ('IO', 'Territorio Británico del Océano Índico'), ('TF', 'Territorios Franceses del Sur'), ('TL', 'Timor Oriental'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad y Tobago'), ('TN', 'Tunez'), ('TM', 'Turkmenistán'), ('TR', 'Turquía'), ('TV', 'Tuvalu'), ('UA', 'Ucrania'), ('UG', 'Uganda'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistán'), ('VU', 'Vanuatu'), ('VE', 'Venezuela, República Bolivariana de'), ('VN', 'Vietnam'), ('WF', 'Wallis y Futuna'), ('YE', 'Yemen'), ('DJ', 'Yibuti'), ('ZM', 'Zambia'), ('ZW', 'Zimbabue')], default='ES', max_length=2, verbose_name='País'),
        ),
    ]