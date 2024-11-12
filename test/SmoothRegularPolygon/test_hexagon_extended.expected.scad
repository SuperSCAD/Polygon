// Unit of length: Unit.MM
$fa = 1.0;
$fs = 0.1;

union()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      difference()
      {
         difference()
         {
            difference()
            {
               difference()
               {
                  polygon(points = [[3.8801, 2.8753], [3.8301, 2.7887], [4.3301, 2.5], [4.3301, 2.5], [4.3301, 2.5], [4.3301, 1.9226], [4.4301, 1.9226], [4.4301, -1.9226], [4.3301, -1.9226], [4.3301, -2.5], [4.3301, -2.5], [4.3301, -2.5], [3.8301, -2.7887], [3.8801, -2.8753], [0.0, -5.1155], [-3.8801, -2.8753], [-3.8301, -2.7887], [-4.3301, -2.5], [-4.3301, -2.5], [-4.3301, -2.5], [-4.3301, -1.9226], [-4.4301, -1.9226], [-4.4301, 1.9226], [-4.3301, 1.9226], [-4.3301, 2.5], [-4.3301, 2.5], [-4.3301, 2.5], [-3.8301, 2.7887], [-3.8801, 2.8753], [0.0, 5.1155]]);
                  translate(v = [4.3301, 2.5])
                  {
                     rotate(a = 300.0)
                     {
                        difference()
                        {
                           polygon(points = [[0.0, 0.1155], [0.55, -0.2021], [0.5, -0.2887], [-0.5, -0.2887], [-0.55, -0.2021]], convexity = 2);
                           translate(v = [0.0, -1.1547])
                           {
                              circle(d = 2.0, $fn = 64);
                           }
                        }
                     }
                  }
               }
               translate(v = [4.3301, -2.5])
               {
                  rotate(a = 240.0)
                  {
                     difference()
                     {
                        polygon(points = [[0.0, 0.1155], [0.55, -0.2021], [0.5, -0.2887], [-0.5, -0.2887], [-0.55, -0.2021]], convexity = 2);
                        translate(v = [0.0, -1.1547])
                        {
                           circle(d = 2.0, $fn = 64);
                        }
                     }
                  }
               }
            }
            translate(v = [-4.3301, -2.5])
            {
               rotate(a = 120.0)
               {
                  difference()
                  {
                     polygon(points = [[0.0, 0.1155], [0.55, -0.2021], [0.5, -0.2887], [-0.5, -0.2887], [-0.55, -0.2021]], convexity = 2);
                     translate(v = [0.0, -1.1547])
                     {
                        circle(d = 2.0, $fn = 64);
                     }
                  }
               }
            }
         }
         translate(v = [-4.3301, 2.5])
         {
            rotate(a = 60.0)
            {
               difference()
               {
                  polygon(points = [[0.0, 0.1155], [0.55, -0.2021], [0.5, -0.2887], [-0.5, -0.2887], [-0.55, -0.2021]], convexity = 2);
                  translate(v = [0.0, -1.1547])
                  {
                     circle(d = 2.0, $fn = 64);
                  }
               }
            }
         }
      }
   }
   difference()
   {
      difference()
      {
         difference()
         {
            difference()
            {
               polygon(points = [[4.3301, 2.5], [4.3301, -2.5], [0.0, -5.0], [-4.3301, -2.5], [-4.3301, 2.5], [0.0, 5.0]]);
               translate(v = [4.3301, 2.5])
               {
                  rotate(a = 300.0)
                  {
                     difference()
                     {
                        polygon(points = [[0.0, 0.1155], [0.55, -0.2021], [0.5, -0.2887], [-0.5, -0.2887], [-0.55, -0.2021]], convexity = 2);
                        translate(v = [0.0, -1.1547])
                        {
                           circle(d = 2.0, $fn = 64);
                        }
                     }
                  }
               }
            }
            translate(v = [4.3301, -2.5])
            {
               rotate(a = 240.0)
               {
                  difference()
                  {
                     polygon(points = [[0.0, 0.1155], [0.55, -0.2021], [0.5, -0.2887], [-0.5, -0.2887], [-0.55, -0.2021]], convexity = 2);
                     translate(v = [0.0, -1.1547])
                     {
                        circle(d = 2.0, $fn = 64);
                     }
                  }
               }
            }
         }
         translate(v = [-4.3301, -2.5])
         {
            rotate(a = 120.0)
            {
               difference()
               {
                  polygon(points = [[0.0, 0.1155], [0.55, -0.2021], [0.5, -0.2887], [-0.5, -0.2887], [-0.55, -0.2021]], convexity = 2);
                  translate(v = [0.0, -1.1547])
                  {
                     circle(d = 2.0, $fn = 64);
                  }
               }
            }
         }
      }
      translate(v = [-4.3301, 2.5])
      {
         rotate(a = 60.0)
         {
            difference()
            {
               polygon(points = [[0.0, 0.1155], [0.55, -0.2021], [0.5, -0.2887], [-0.5, -0.2887], [-0.55, -0.2021]], convexity = 2);
               translate(v = [0.0, -1.1547])
               {
                  circle(d = 2.0, $fn = 64);
               }
            }
         }
      }
   }
}
