document.getElementById("dataForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value;

  const response = await fetch("/data", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name }),
  });

  const result = await response.json();
  document.getElementById("response").textContent = result.message || result.error;
});