// Unit of length: Unit.MM
$fa = 1.0;
$fs = 0.1;

difference()
{
   difference()
   {
      difference()
      {
         polygon(points = [[0.0, 0.0], [0.0, 0.0], [0.0, 1.0], [-0.1, 1.0], [-0.1, 8.382], [0.0, 8.382], [0.0, 10.0], [20.0, 0.0]]);
         rotate(a = 135.0)
         {
            difference()
            {
               polygon(points = [[0.0, 0.1414], [0.7778, -0.6364], [0.7071, -0.7071], [-0.7071, -0.7071], [-0.7778, -0.6364]], convexity = 2);
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
               polygon(points = [[-0.0851, 0.0526], [0.0, 0.1], [0.0851, 0.0526], [0.9357, -1.3238], [0.8507, -1.3764], [-0.8507, -1.3764], [-0.9357, -1.3238]], convexity = 2);
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
            polygon(points = [[-0.0973, 0.023], [0.0, 0.1], [0.0973, 0.023], [1.0706, -4.0998], [0.9732, -4.1227], [-0.9732, -4.1227], [-1.0706, -4.0998]], convexity = 2);
            translate(v = [0.0, -4.3525])
            {
               circle(d = 2.0, $fn = 64);
            }
         }
      }
   }
}
