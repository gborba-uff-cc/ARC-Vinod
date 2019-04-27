export function simualadorRoteamento(){

    if (tabelaRoteamento.length === 0){
        console.log("[ALERT] Nenhum roteador foi registrado");
        conectado = 0;
        err.push('404');
        return '0';
    }

    else{
        //Switch do Roteador
        if (random(30) >= 25){
            console.log("[WARNING] Conexão Ruim");
            //Reconexão:
            console.log("Estabelecendo nova conexão");
            for (var i = 0; i < tabelaRoteamento.length; ++i){
                if (tabelaRoteamento[i] !== conectado){
                    console.log("Tentando conexão com "+tabelaRoteamento[i]);
                    if (random(30) <= 10){
                        conectado = tabelaRoteamento[i];
                        flagLigado = true;
                        return conectado;
                    }
                }
                if (i === tabelaRoteamento.length-1){
                    console.log("[ALERT] Nenhum acess point adequeado");
                    err.push('405');
                    return 0;
                }
            }
        }
        return conectado;
    }
}