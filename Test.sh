# Define an array of planets
planets=(Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Pluto)
# Print the array
echo ${planets[@]}
# Print the array with the index
echo ${!planets[@]}
# Print the number of elements in the array
echo ${#planets[@]}
# Print the length of the first element
echo ${#planets[0]}
# Print the length of the last element
echo ${#planets[-1]}
# Display "My very educated mother just served us nine pizzas"
echo ${planets[@]:0:9}