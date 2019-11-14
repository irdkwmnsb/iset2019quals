#!/bin/sh
mysql -uroot -pnoonewillseeitanywaysonothingcomesuphere -e "GRANT SELECT ON \`app\`.\`flags\` TO 'webuser'@'%' IDENTIFIED BY 'xxx_diphop_p455_xxx';";