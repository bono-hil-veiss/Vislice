% rebase('base.tpl')

<h1>Seznam že končanih iger:</h1>

<!--
Naredite <ul>...</ul> (unordered list), v njem pa s for zanko <li>-je (list item), ki bodo prikazovali
id-je preteklih iger, ter nas ob kliku nanje preusmerili na ustrezen url.

Pod seznamom lahko dodate še gumb DOMOV, ki nas preusmeri na začetno stran.
-->

<ul>
% for id_igre, (igre, stanje) in igre.items():
  <li> <a href="http://127.0.0.1:8080/igra/{{id_igre}}">
        Igra {{id_igre}} (stanje: {{stanje}})
    </a> 
  </li>
% end
</ul>

<form action="/" method="get">
  <button type="submit">DOMOV</button>
</form>