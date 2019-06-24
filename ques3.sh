#!/bin/bash
apt install -y apache2
cat > /var/www/html/index.html << EOF
</html>
<body>
Anisha
</body>
</html>
EOF


