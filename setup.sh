#!/bin/bash
export AUTH0_DOMAIN="dev-t7m1o5rxtdqtdtwb.us.auth0.com"
export ALGORITHMS='RS256'
export API_AUDIENCE="capstone"

export DATABASE_URL="postgresql://postgres:Subhiksha@localhost:5432/capstone"

echo "setup.sh script executed successfully!"
echo $DATABASE_URL