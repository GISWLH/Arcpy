> Copyright © 2022 Longhao Wang hhuwlh@163.com All rights reserved.
>
> This work is licensed under the terms of the MIT license.  
>
> or a copy, see <https://opensource.org/licenses/MIT>.

Data description

* input: Beijing DEM and my tool box.

* map: output map. see task (3), you can delete all the file to generate your own file.
* output: output file (also the work space)
* code:

| code          | description                                                  |
| ------------- | ------------------------------------------------------------ |
| 1creat_region | Create a DEM map box                                         |
| 2clip         | Clip the region to avoid the out points                      |
| 3random_point | Create 200 points randomly and their field                   |
| 4extract_dem  | Extract DEM of 200 points                                    |
| creat_table   | The task (1) all code. To create my own Tool (input: excel, output: shp) |
| spline        | The task (2) all code. To do the spline interpolation        |
| grid          | To generate the grid to create the map                       |
| creat_map     | The task (3) code to create the map                          |

* data: This is equal to the "地质调查点基础数据表.xls", but English name
* MapID: The graphic illustration of number of map 
* workspace: The mxd file.
* LICENSE: Copyright © 2022 Longhao Wang hhuwlh@163.com All rights reserved.