// Unit of length: Unit.MM
$fa = 1.0;
$fs = 0.1;

union()
{
   difference()
   {
      square(size = [20.0, 10.0], center = false);
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
      translate(v = [0.0, 10.0])
      {
         rotate(a = 45.0)
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
      translate(v = [20.0, 10.0])
      {
         rotate(a = 315.0)
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
      translate(v = [20.0, 0.0])
      {
         rotate(a = 225.0)
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
   }
}
