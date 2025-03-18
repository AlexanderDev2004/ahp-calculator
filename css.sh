if ! npx tailwindcss -v > /dev/null 2>&1 || ! npx postcss -v > /dev/null 2>&1;
then
    npm install postcss tailwindcss @tailwindcss/cli @tailwindcss/postcss
fi

if [ ! -f "./public/css/output.css" ];
then
    touch ./public/css/output.css
    echo '@import "tailwindcss";' > ./public/css/output.css
else
    if ! grep -q '@import "tailwindcss";' ./public/css/output.css;
    then
        echo '@import "tailwindcss";' >> ./public/css/output.css
    fi
fi

npx @tailwindcss/cli -i ./public/css/output.css -o ./public/css/output.css --watch