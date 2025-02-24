using
System;
using
System.Collections.Generic;
using
System.Linq;


class Program
    {
        static
    void
    Main()
    {
    // Generar
    el
    conjunto
    de
    ciudadanos
    HashSet < string > ciudadanos = new
    HashSet < string > ();
    for (int i = 1; i <= 500; i++)
    {
        ciudadanos.Add($"Ciudadano {i}");
    }

    // Generar conjuntos de vacunados con Pfizer y AstraZeneca
    HashSet < string > vacunadosPfizer = new HashSet < string > (ciudadanos.OrderBy(x = > Guid.NewGuid()).Take(75));
    HashSet < string > vacunadosAstrazeneca = new HashSet < string > (ciudadanos.Except(vacunadosPfizer).OrderBy(x = > Guid.NewGuid()).Take(75));

    // Listado de ciudadanos que han recibido ambas vacunas
    HashSet < string > vacunadosAmbas = new HashSet < string > (vacunadosPfizer.Intersect(vacunadosAstrazeneca));

    // Listado de ciudadanos que no se han vacunado
    HashSet < string > noVacunados = new HashSet < string > (ciudadanos.Except(vacunadosPfizer.Union(vacunadosAstrazeneca)));

    // Listado de ciudadanos vacunados solo con Pfizer
    HashSet < string > soloPfizer = new HashSet < string > (vacunadosPfizer.Except(vacunadosAstrazeneca));

    // Listado de ciudadanos vacunados solo con Astrazeneca
    HashSet < string > soloAstrazeneca = new HashSet < string > (vacunadosAstrazeneca.Except(vacunadosPfizer));

    // Mostrar resultados
    Console.WriteLine("Listado de ciudadanos no vacunados: " + noVacunados.Count);
    Console.WriteLine("Listado de ciudadanos con ambas vacunas: " + vacunadosAmbas.Count);
    Console.WriteLine("Listado de ciudadanos vacunados solo con Pfizer: " + soloPfizer.Count);
    Console.WriteLine("Listado de ciudadanos vacunados solo con Astrazeneca: " + soloAstrazeneca.Count);
    }
    }
