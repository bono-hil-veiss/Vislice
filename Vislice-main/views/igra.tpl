% rebase('base.tpl')

<h1>Igra Vislic</h1>

<p>Nepravilne črke: {{igra.nepravilni_ugibi()}} </p>

<p>Pravilni del gesla: {{igra.pravilni_del_gesla()}} </p>

%if igra.zmaga():
<p>ČESTITKE, MISIJA JE KONČANA!</p>
%elif igra.poraz():
<p>Igre je žal konec. Prava beseda je {{igra.geslo}}</p>
<img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">
%else:
<p>Stopnja obešenosti:</p>
<img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">
%end

%if not igra.zmaga() and not igra.poraz():
  <form action="/igra/{{id_igre}}" method="post">
      Ugibana črka: <input name="crka" type="text" maxlength="1"/>
      <button type="submit" value="bla" name="xy">UGIBAJ</button>
  </form>
  <form action="/igra/" method="post">
    %for i, vrsta in enumerate(tipkovnica):
       <div class="vrsta{{i}}">
    %  for crka in vrsta:
           <button class="gumb_crka" type="submit" name="crka" value="{{crka}}">{{crka}}</button>\\
    %  end
       </div>
    %end
  </form>
%else:
 <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
</form>
%end



