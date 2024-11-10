// Unit of length: Unit.MM
$fa = 1.0;
$fs = 0.1;

difference()
{
   union()
   {
      difference()
      {
         difference()
         {
            polygon(points = [[0.0, 20.0], [10.0, 0.0], [0.0, 10.0], [-10.0, 0.0]]);
            translate(v = [0.0, 20.0])
            {
               difference()
               {
                  polygon(points = [[0.0, 0.01], [0.9044, -1.7889], [-0.9044, -1.7889]], convexity = 2);
                  translate(v = [0.0, -2.2361])
                  {
                     circle(d = 2.0, $fn = 64);
                  }
               }
            }
         }
         translate(v = [10.0, 0.0])
         {
            rotate(a = 215.7825)
            {
               difference()
               {
                  polygon(points = [[0.0, 0.01], [0.9971, -6.0827], [-0.9971, -6.0827]], convexity = 2);
                  translate(v = [0.0, -6.2429])
                  {
                     circle(d = 2.0, $fn = 64);
                  }
               }
            }
         }
      }
      translate(v = [0.0, 10.0])
      {
         difference()
         {
            polygon(points = [[0.0, 0.01], [0.7171, -0.7071], [-0.7171, -0.7071]], convexity = 2);
            translate(v = [0.0, -1.4142])
            {
               circle(d = 2.0, $fn = 64);
            }
         }
      }
   }
   translate(v = [-10.0, 0.0])
   {
      rotate(a = 144.2175)
      {
         difference()
         {
            polygon(points = [[0.0, 0.01], [0.9971, -6.0827], [-0.9971, -6.0827]], convexity = 2);
            translate(v = [0.0, -6.2429])
            {
               circle(d = 2.0, $fn = 64);
            }
         }
      }
   }
}
