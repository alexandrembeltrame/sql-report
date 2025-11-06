// src/services/api.ts

// ✅ O proxy do Vite já encaminha /reports para o backend (localhost:8000)
// então não precisamos mais do import.meta.env aqui

export async function fetchEmployees() {
  try {
    const response = await fetch("/reports/employees"); // o proxy do Vite cuida do host

    if (!response.ok) {
      console.error("❌ Erro HTTP:", response.status, response.statusText);
      throw new Error("Erro ao buscar relatório de funcionários");
    }

    const data = await response.json();
    console.log("✅ Dados recebidos:", data);
    return data;
  } catch (err) {
    console.error("❌ Erro de fetch:", err);
    throw err;
  }
}
