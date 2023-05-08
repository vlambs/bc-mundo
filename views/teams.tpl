% rebase('base.tpl', title='Teams')

<h1>Teams</h1>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Members</th>
    </tr>
  </thead>
  <tbody>
    % for team in teamsList:
    <tr>
      <td>{{team['name']}}</td>
      <td>
        <ul>
          % for member in team['members']:
          <li>{{member['name']}} - {{member['age']}} y.o - {{member['height']}}m - {{member['position']}}</li>
          % end
        </ul>
      </td>
    </tr>
    % end
  </tbody>
</table>