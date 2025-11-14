export async function fetchEmployees() {
  try {
    const response = await fetch("/api/reports/employees");

    if (!response.ok) {
      throw new Error("Erro ao buscar relatório de funcionários");
    }

    const data = await response.json();
    console.log("✅ Dados recebidos employees:", data);

    return {
      results: Array.isArray(data.results) ? data.results : [],
    };
  } catch (err) {
    console.error("❌ Erro de fetch employees:", err);
    throw err;
  }
}

export async function fetchFinances() {
  try {
    const response = await fetch("/api/finances");

    if (!response.ok) {
      throw new Error("Erro ao buscar relatório financeiro");
    }

    const data = await response.json();
    console.log("✅ Dados financeiros recebidos:", data);

    return data;
  } catch (err) {
    console.error("❌ Erro de fetch finances:", err);
    throw err;
  }
}
