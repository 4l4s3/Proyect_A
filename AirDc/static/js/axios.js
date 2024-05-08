const productosApi = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/productos",
});

async function getProducto(id) {
  const hi = await productosApi.delete(`/${id}`);
  console.log(hi.data);
}
