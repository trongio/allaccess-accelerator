#!/bin/bash

# Ensure bash array and associative array support (requires bash 4+)
if [ -z "${BASH_VERSINFO}" ] || [ "${BASH_VERSINFO[0]}" -lt 4 ]; then
    echo "This script may not work properly in Bash version <4."
fi

HEADERS=(
    -H 'Referer: https://fontawesome.com'
)
API_URL="https://api.github.com/repos/FortAwesome/Font-Awesome/releases/latest"

get_latest_version() {
    curl -s -H "Accept: application/vnd.github.v3+json" "$API_URL" | grep -oE '"tag_name": *"[^"]+"' | sed -E 's/.*"([^"]+)".*/\1/'
}

fetch() {
    local url="$1"
    local out_path="$2"
    curl -s -f -L "${HEADERS[@]}" -o "$out_path" --create-dirs "$url"
}

main() {
    local version
    version=$(get_latest_version)
    if [ -z "$version" ]; then
        echo "Failed to get latest version from GitHub."
        exit 1
    fi
    echo "Latest Font Awesome Pro version: $version"

    local css_files=(
        "all.css" "solid.css" "regular.css" "light.css" "thin.css"
        "duotone.css" "duotone-regular.css" "duotone-light.css" "duotone-thin.css"
        "sharp-solid.css" "sharp-regular.css" "sharp-light.css" "sharp-thin.css"
        "sharp-duotone-solid.css" "sharp-duotone-regular.css" "sharp-duotone-light.css" "sharp-duotone-thin.css"
        "brands.css" "chisel-regular.css" "etch-solid.css" "graphite-thin.css"
        "jelly-regular.css" "jelly-duo-regular.css" "jelly-fill-regular.css"
        "mosaic-solid.css" "notdog-solid.css" "notdog-duo-solid.css" "pixel-regular.css"
        "slab-regular.css" "slab-press-regular.css" "slab-duo-regular.css" "slab-press-duo-regular.css"
        "thumbprint-light.css" "utility-semibold.css" "utility-fill-semibold.css" "utility-duo-semibold.css"
        "vellum-solid.css" "whiteboard-semibold.css"
    )

    declare -A fetched_urls

    for css_file in "${css_files[@]}"; do
        local base_url="https://site-assets.fontawesome.com/releases/v${version}/css/${css_file}"
        local base_path="css/${css_file}"

        mkdir -p "$(dirname "$base_path")"
        echo -e "\n[$css_file] Fetching $base_url to $base_path..."

        if ! fetch "$base_url" "$base_path"; then
            echo "  -> Failed to fetch $css_file"
            continue
        fi

        # Extract URLs from url(...) patterns, strip quotes
        local urls
        urls=$(grep -oE 'url\([^)]+\)' "$base_path" | sed -E "s/url\(|\)|[\"']//g")
        
        # Get unique URLs
        local unique_urls
        if [ -n "$urls" ]; then
            unique_urls=$(echo "$urls" | sort -u)
        else
            unique_urls=""
        fi

        for u in $unique_urls; do
            # Skip inline data URIs
            if [[ "$u" == data:* ]]; then
                continue
            fi
            
            local fetch_url
            local out_path

            if [[ "$u" == http://* || "$u" == https://* || "$u" == //* ]]; then
                fetch_url="$u"
                if [[ "$u" == //* ]]; then
                    fetch_url="https:$u"
                fi
                # Dynamically handle absolute http(s) URL
                local url_path
                url_path="${fetch_url%%\?*}"
                url_path="${url_path%%\#*}"
                local filename
                filename=$(basename "$url_path")
                out_path="$(dirname "$base_path")/$filename"
            else
                # Dynamically handle relative path (eg. css/../webfonts -> webfonts)
                local u_path
                u_path=$(realpath -m "/css/$u")
                fetch_url="https://site-assets.fontawesome.com/releases/v${version}${u_path}"
                out_path=$(realpath -m --relative-to="." "css/$u")
            fi

            if [[ -n "${fetched_urls["$fetch_url"]}" ]]; then
                continue
            fi

            mkdir -p "$(dirname "$out_path")"
            if [ ! -f "$out_path" ]; then
                echo "  -> Fetching asset $fetch_url to $out_path..."
                if fetch "$fetch_url" "$out_path"; then
                    fetched_urls["$fetch_url"]=1
                else
                    echo "  -> Failed to fetch asset: $fetch_url"
                fi
            else
                fetched_urls["$fetch_url"]=1
            fi
        done
    done
}

main
