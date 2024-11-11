// Unit of length: Unit.MM
$fa = 1.0;
$fs = 0.1;

difference()
{
   difference()
   {
      difference()
      {
         polygon(points = [[0.0, 0.0], [0.0, 10.0], [20.0, 0.0]]);
         rotate(a = 135.0)
         {
            difference()
            {
               polygon(points = [[0.0, 0.0141], [0.7142, -0.7], [0.7071, -0.7071], [-0.7071, -0.7071], [-0.7142, -0.7]], convexity = 2);
               translate(v = [0.0, -1.4142])
               {
                  circle(d = 2.0, $fn = 64);
               }
            }
         }
      }
      translate(v = [0.0, 10.0])
      {
         rotate(a = 31.7175)
         {
            difference()
            {
               polygon(points = [[-0.0085, 0.0053], [0.0, 0.01], [0.0085, 0.0053], [0.8592, -1.3711], [0.8507, -1.3764], [-0.8507, -1.3764], [-0.8592, -1.3711]], convexity = 2);
               translate(v = [0.0, -1.9021])
               {
                  circle(d = 2.0, $fn = 64);
               }
            }
         }
      }
   }
   translate(v = [20.0, 0.0])
   {
      rotate(a = 256.7175)
      {
         difference()
         {
            polygon(points = [[-0.0097, 0.0023], [0.0, 0.01], [0.0097, 0.0023], [0.983, -4.1205], [0.9732, -4.1227], [-0.9732, -4.1227], [-0.983, -4.1205]], convexity = 2);
            translate(v = [0.0, -4.3525])
            {
               circle(d = 2.0, $fn = 64);
            }
         }
      }
   }
}
